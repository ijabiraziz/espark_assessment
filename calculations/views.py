import pandas as pd
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import calculate_columns


@api_view(["POST"])
def upload_file(request):
    if "file" not in request.FILES:
        return Response(
            {"error": "No file part"}, status=status.HTTP_400_BAD_REQUEST
        )

    file = request.FILES["file"]
    if file.name == "":
        return Response(
            {"error": "No selected file"}, status=status.HTTP_400_BAD_REQUEST
        )

    allowed_file_types = (".xls", ".xlsx")
    if file.name.endswith(allowed_file_types):
        df = pd.read_excel(file, engine="openpyxl")
        # print("Columns in the uploaded file:", df.columns)
        df.columns = df.columns.str.strip()

        # Check if 'Input' exists (it is Simple COlumn C)
        if "Input" not in df.columns:
            return Response(
                {"error": "Input column not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Call util function
        df = calculate_columns(df)

        file_name = file.name.split(".")
        output_file = f"{file_name[0]}_result.csv"
        df.to_csv(output_file, index=False)
        return Response(
            {
                "message": "File processed successfully",
                "output_file": output_file,
            },
            status=status.HTTP_200_OK,
        )
    return Response(
        {"error": "Invalid file type"}, status=status.HTTP_400_BAD_REQUEST
    )
