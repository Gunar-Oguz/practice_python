import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/ageron/handson-ml2/refs/heads/master/datasets/housing/housing.csv"
housing = pd.read_csv(url)
print("Shape is; ", housing.shape)
print(housing.head(5))
print(housing.columns.to_list())
print(housing.dtypes)
print(housing.info())
print(housing.describe())
print(housing.columns.to_list())
print(housing["median_income"].min())
print(housing["median_income"].max())
print(housing["median_income"].mean())
print(housing["total_bedrooms"].value_counts())
print(housing["total_bedrooms"].nunique())
print(housing["median_income"].nunique())
print(housing["median_income"].std())
print(housing.isnull().sum())
print(housing.isnull().sum().sum())
print(housing.isnull().sum() / len(housing) * 100)
print(housing["total_bedrooms"].isna())
print(housing[housing["total_bedrooms"].isna()])
print(housing["ocean_proximity"])
print(housing[["ocean_proximity"]])
print(housing[["median_income" ,"ocean_proximity"]])
print(housing.columns.to_list())
print(housing.latitude)
print(housing.median_income)
print(housing.iloc[0])
print(housing.iloc[-1])
print(housing.iloc[0:5])
print(housing.iloc[[0,2,4]])
print(housing.iloc[0:5, 0:3])
print(housing.iloc[:, -1])
print(housing.loc[1])
print((housing["housing_median_age"] > 30).sum())
print(housing[housing["ocean_proximity"] == "NEAR BAY"])
print(housing[housing["ocean_proximity"] != "NEAR BAY"])
print(housing[(housing["housing_median_age"] > 30) & (housing["ocean_proximity"] == "INLAND")])
print(housing[housing["ocean_proximity"].isin(["NEAR BAY", "INLAND"])])
print(housing[housing["ocean_proximity"].isin(["NEAR BAY"])])
print(housing[~housing["ocean_proximity"].isin(["NEAR BAY", "INLAND"])])
print("20 to 30 years old houses: ", housing[housing["housing_median_age"].between(20, 30)])

housing["new_column"] = 0
print(housing.head(5))
print(housing.columns.to_list())
housing["all_rooms"] = housing["total_bedrooms"] + housing["total_rooms"]
print(housing.head(5))
housing['house_value_per_household'] = housing["median_house_value"] / housing["households"]
print(housing.head())
housing["double_med_income"] = housing["median_income"].apply(lambda x: x * 2)
print(housing.head())
housing["age_category"] = np.where(housing["housing_median_age"] > 30, "old", "young")
print(housing.head())
print(housing.head(3))

print(housing.columns.to_list())

# print(np.where(housing["median_income"] > 5))
print(housing[housing["median_income"] > 5]\
      .head(5))

print(housing\
      .groupby("ocean_proximity")["median_house_value"]\
      .mean()\
      .round(2)
      .reset_index()\
      .rename(columns = {"median_house_value": "average_value"}))

print("size counts: " ,housing[housing["housing_median_age"] > 30]\
.groupby("ocean_proximity").size())

print("count counts: " , housing[housing["housing_median_age"] > 30]\
.groupby("ocean_proximity").count())

print(housing.sort_values("median_house_value", ascending=False))


print(housing[housing["total_rooms"] > 1000]\
.groupby("ocean_proximity")\
["median_income"].mean())

print(housing[housing["ocean_proximity"] == "ISLAND"].head())

print(housing[housing["median_income"] < 2].head(10))

print(housing[housing["ocean_proximity"] != "INLAND"].head(7))

print(housing[((housing["housing_median_age"] > 40) & (housing["median_income"] > 5))].head(5))

print(housing[(housing["ocean_proximity"] == "NEAR BAY") | (housing["ocean_proximity"] == "NEAR OCEAN")].head(6))

print(housing[housing["median_house_value"] > 400000].shape[0])
print(housing[housing["ocean_proximity"] == "INLAND"].shape[0])

print(housing[(housing["total_rooms"] > 5000) & (housing["median_income"] < 3)].shape[0])

print("houses between 20 and 30: ", housing[housing["housing_median_age"].between(20, 30)].shape[0])

print(housing.groupby("ocean_proximity")["median_house_value"].mean())

print(housing.groupby("ocean_proximity")["population"].sum())

print("counting: ", housing.groupby("ocean_proximity").size())

print(housing.groupby("ocean_proximity")["total_rooms"].mean())

print(housing[housing["median_income"] > 5]\
.groupby("ocean_proximity")\
["median_house_value"].mean())

print(housing[housing["housing_median_age"] > 40]\
.groupby("ocean_proximity")\
["median_income"].mean())

print(housing[housing["total_rooms"] < 2000]\
.groupby("ocean_proximity")\
["population"].sum())

print(housing[housing["total_rooms"] < 2000]\
.groupby("ocean_proximity")\
["population"].sum())

print(
    "max_median_value: " , housing[housing["ocean_proximity"] == "INLAND"]\
.groupby("housing_median_age")\
["median_house_value"].max())

print(housing[housing["median_income"].between(3,6)]\
.groupby("ocean_proximity").size())

print([housing["median_income"]])

print("ocean proximity: ", housing["ocean_proximity"])


print(housing[housing["population"] > 1000]\
.groupby("ocean_proximity")\
["total_bedrooms"].mean())

print(housing.sort_values("median_house_value", ascending=True).head(10))

print(housing.sort_values("latitude", ascending = False).head(10))

print(housing.sort_values("median_income", ascending = False).head(5))

print(housing.sort_values("median_income", ascending=False).head(5))

print(housing.groupby("ocean_proximity")["median_house_value"]\
      .mean()\
      .sort_values(ascending = False))

print(
    housing[housing["housing_median_age"] > 30]\
    .groupby("ocean_proximity")\
    .sum("population")\
    .sort_values("population", ascending=False)
)

print(
    housing[housing["median_income"] > 4]\
    .groupby("ocean_proximity")\
    .mean("median_house_value")\
    .sort_values("median_house_value", ascending=True)
)

print(
    housing[housing["total_bedrooms"] > 500]\
    .groupby("ocean_proximity")["median_house_value"]\
    .max()\
    .sort_values(ascending=False)
)

print(
    housing[housing["median_income"] > 3]\
    .groupby("ocean_proximity")["housing_median_age"]\
    .min()
)

print(
    housing[housing["housing_median_age"] > 20]\
    .groupby("ocean_proximity")[["median_income", "median_house_value"]]\
    .mean()\
    .sort_values("median_house_value", ascending=False)
    )

print(
    housing[housing["ocean_proximity"] != "INLAND"]\
    .groupby("ocean_proximity")["households"]\
    .sum()\
    .sort_values(ascending=True)
)





















