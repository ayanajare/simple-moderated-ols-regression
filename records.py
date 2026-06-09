import pandas as pd


COLUMNS_MAPPPING : dict = {
    'Q1_1': 'perceived_information_reliance_on_llm_a',
    'Q1_2': 'perceived_information_reliance_on_llm_b',
    'Q1_3': 'perceived_information_reliance_on_llm_c',
    'Q2_1': 'perceived_trustworthiness_among_teams_a',
    'Q2_2': 'perceived_trustworthiness_among_teams_b',
    'Q2_3': 'perceived_trustworthiness_among_teams_c',
    'Q2_4': 'perceived_trustworthiness_among_teams_d',
    'Q3_1': 'perceived_team_performance_a',
    'Q3_2': 'perceived_team_performance_b',
    'Q3_3': 'perceived_team_performance_c',
    'Q4' : 'age_range',
    'Q5' : 'academic_level',
    'Q6' : 'frequency_group_assignments',
    'Q7' : 'definition_llm',
    'Q7_5_TEXT' : 'definition_llm_text',
    'Q8' : 'academic_field',
    'Q8_5_TEXT' : 'academic_field_text',
    'Q9' : 'frequency_llm_usage_assignments',
    'Q10' : 'purpose_llm_usage',
    'Q10_7_TEXT' : 'purpose_llm_usage_text'
}


ALL_CONSTRUCTS : list = [
    'perceived_information_reliance_on_llm_a',
    'perceived_information_reliance_on_llm_b',
    'perceived_information_reliance_on_llm_c',
    'perceived_trustworthiness_among_teams_a',
    'perceived_trustworthiness_among_teams_b',
    'perceived_trustworthiness_among_teams_c',
    'perceived_trustworthiness_among_teams_d',
    'perceived_team_performance_a',
    'perceived_team_performance_b',
    'perceived_team_performance_c',
]

CONSTRUCTS : dict = {
    "perceived_information_reliance_on_llm": [
        'perceived_information_reliance_on_llm_a',
        'perceived_information_reliance_on_llm_b',
        'perceived_information_reliance_on_llm_c'
    ],
    "perceived_trustworthiness_among_teams": [
        'perceived_trustworthiness_among_teams_a',
        'perceived_trustworthiness_among_teams_b',
        #'perceived_trustworthiness_among_teams_c',
        'perceived_trustworthiness_among_teams_d'
    ],
    "perceived_team_performance": [
        'perceived_team_performance_a',
        'perceived_team_performance_b',
        'perceived_team_performance_c'
    ]
}

DEMOGRAPHIC_VARIABLES : list = [
    'age_range',
    'academic_level',
    'frequency_group_assignments',
    'definition_llm',
    'definition_llm_text',
    'academic_field',
    'academic_field_text',
    'frequency_llm_usage_assignments',
    'purpose_llm_usage',
    'purpose_llm_usage_text'
]



def rename_columns(df: pd.DataFrame, columns_mapping : dict = COLUMNS_MAPPPING) -> pd.DataFrame:
    return df.rename(columns=columns_mapping)


def filter_valid_records(df: pd.DataFrame) -> pd.DataFrame:
    df_1 = df[1:]  # Remove the first row
    df_2 = df_1[df_1["DistributionChannel"] != "preview"]  # Exclude preview responses
    df_3 = df_2[df_2["Progress"] == 100]  # Include only completed responses
    df_3["perceived_trustworthiness_among_teams_c"] = df_3["perceived_trustworthiness_among_teams_c"].replace({1: 5, 2: 4, 4: 2, 5: 1})
    return df_3

def get_clean_data(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path)
    df_rename = rename_columns(df)
    df_valid = filter_valid_records(df_rename)
    return df_valid

def get_constructs_data(df: pd.DataFrame, constructs : list = ALL_CONSTRUCTS) -> pd.DataFrame:
    df[constructs] = df[constructs].apply(pd.to_numeric, errors='coerce')
    return df[constructs]

