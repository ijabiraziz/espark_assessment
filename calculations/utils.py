def calculate_columns(df):
    # Initialize columns
    df['D'] = 0
    df['E'] = 0
    df['F'] = 0
    df['G'] = 0
    df['H'] = 0
    df['I'] = 0
    df['J'] = 0

    for i in range(1, len(df)):
        df.at[i, 'D'] = df.at[i, 'Input'] - df.at[i - 1, 'Input']  # Use 'Input'
        df.at[i, 'E'] = max(df.at[i, 'D'], 0)
        df.at[i, 'F'] = max(-df.at[i, 'D'], 0)

        if i < 14:
            df.at[i, 'G'] = df['E'][:i + 1].sum() / (i + 1)
            df.at[i, 'H'] = df['F'][:i + 1].sum() / (i + 1)
        else:
            df.at[i, 'G'] = (df.at[i - 1, 'G'] * 13 + df.at[i, 'E']) / 14
            df.at[i, 'H'] = (df.at[i - 1, 'H'] * 13 + df.at[i, 'F']) / 14

        df.at[i, 'I'] = df.at[i, 'G'] / df.at[i, 'H'] if df.at[i, 'H'] != 0 else 0
        df.at[i, 'J'] = 100 if df.at[i, 'H'] == 0 else 100 - (100 / (1 + df.at[i, 'I']))

    return df