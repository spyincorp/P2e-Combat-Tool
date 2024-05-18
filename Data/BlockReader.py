import json
import glob
from datetime import datetime
import csv
import os
import pandas as pd


def beastiary_to_dataframe():

    subdirectories = [
        "Library\\pathfinder-bestiary",
        "Library\\pathfinder-bestiary-2",
        "Library\\pathfinder-bestiary-3",
    ]

    data = [
        [
            "Name",
            "Level",
            "Traits",
            "AC",
            "HP",
            "Speed",
            "Cha",
            "Con",
            "Dex",
            "Int",
            "Str",
            "Wis",
        ]
    ]

    for sub in subdirectories:
        files = glob.glob(f"{sub}/*.json", recursive=True)

        for single_file in files:
            with open(single_file, "r", encoding="utf-8") as f:
                try:
                    json_file = json.load(f)
                    name = json_file.get("name", "")
                    level = (
                        json_file.get("system", "")
                        .get("details", "")
                        .get("level", "")
                        .get("value", "")
                    )
                    traits = (
                        json_file.get("system", "").get("traits", "").get("value", "")
                    )
                    ac = (
                        json_file.get("system", "")
                        .get("attributes", "")
                        .get("ac", "")
                        .get("value", "")
                    )
                    hp = (
                        json_file.get("system", "")
                        .get("attributes", "")
                        .get("hp", "")
                        .get("value", "")
                    )
                    speed = (
                        json_file.get("system", "")
                        .get("attributes", "")
                        .get("speed", "")
                        .get("value", "")
                    )
                    cha = (
                        json_file.get("system", "")
                        .get("abilities", "")
                        .get("cha", "")
                        .get("mod", "")
                    )
                    con = (
                        json_file.get("system", "")
                        .get("abilities", "")
                        .get("con", "")
                        .get("mod", "")
                    )
                    dex = (
                        json_file.get("system", "")
                        .get("abilities", "")
                        .get("dex", "")
                        .get("mod", "")
                    )
                    int = (
                        json_file.get("system", "")
                        .get("abilities", "")
                        .get("int", "")
                        .get("mod", "")
                    )
                    str = (
                        json_file.get("system", "")
                        .get("abilities", "")
                        .get("str", "")
                        .get("mod", "")
                    )
                    wis = (
                        json_file.get("system", "")
                        .get("abilities", "")
                        .get("wis", "")
                        .get("mod", "")
                    )

                    if name:
                        data.append(
                            [
                                name,
                                level,
                                traits,
                                ac,
                                hp,
                                speed,
                                cha,
                                con,
                                dex,
                                int,
                                str,
                                wis,
                            ]
                        )
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {single_file}: {e}")
                    continue

    df = pd.DataFrame(data[1:], columns=data[0])
    df["Level"] = pd.to_numeric(
        df["Level"], errors="coerce"
    )  # Convert 'Level' column to numeric for sorting

    # Sort DataFrame by 'Level' column
    df_sorted = df.sort_values(by=["Level", "Name"])

    return df_sorted


def dataframe_to_csv():
    df = beastiary_to_dataframe()
    output_dir = os.path.join("Data", "BeastiaryCsv")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "Beastiary.csv")
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    dataframe_to_csv()
