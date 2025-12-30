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

print(housing.isna().sum())

print(housing.isna())

print(housing[housing["total_bedrooms"].isna()])

print(housing["total_bedrooms"].isna().sum())

housing_clean = housing.dropna(subset = ["total_bedrooms"])

print(housing_clean)
print(housing_clean["total_bedrooms"].isna().sum())

print(housing["total_bedrooms"].isna().sum())

housing_replaced = housing["total_bedrooms"].fillna(0)
print(housing_replaced.isna().sum())

housing["total_bedrooms_filled"] = housing["total_bedrooms"].fillna(housing["total_bedrooms"].mean())
print(housing.groupby("ocean_proximity")["total_bedrooms_filled"].mean())

housing["country"] = "USA"
print(housing.head())

housing["state"] = "California"
print(housing.head())

housing["data_source"] = "california_census"
print(housing.head())
print(housing.columns.to_list())

housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
print(housing.head())

housing["people_per_household"] = housing["population"] / housing["households"]

print(housing.head())

housing["age_category"] = np.where(
    housing["housing_median_age"] > 30,
      "old", "new")
housing["income_level"] = np.where(
    housing["median_income"] > 5, "high", "low"

)
print(housing.head())
housing["half_income"] = housing["median_income"].apply(lambda x: x * 2)
print(housing.head())

housing["income_category"] = housing["median_income"]\
.apply(lambda x: "low" if x < 3 else ("medium" if x < 6 else "high"))

print(housing.head(0))

housing["ocean_proximity"].replace("INLAND", "INTERIOR")
print(housing.head(10))

housing["income_category"] = housing["income_category"].replace("high", "very_high")
print(housing.head())

housing = housing.rename(columns = {"median_income": "med_income"})
print(housing.head(5))
housing = housing.rename(columns = {'housing_median_age': "housing_age"})
print(housing.head())

housing = housing.drop("country", axis = 1)
print(housing.columns.to_list())

housing = housing.drop("data_source", axis = 1)
print(housing.columns.to_list())

print(housing.nlargest(10, "half_income"))

print(housing.loc[0, "half_income"])

print(housing.dtypes)

housing["housing_age"] = housing["housing_age"].astype(int)
print(housing.dtypes)

print(housing["ocean_proximity"].value_counts())

print(housing.columns.to_list())
print(housing["income_level"].value_counts())

print(round(housing["income_category"].value_counts(normalize = True), 1))

print(housing[housing["income_level"] == "high"]\
.groupby("ocean_proximity")["median_house_value"]\
.mean()\
.sort_values(ascending=False))

print(housing[housing["people_per_household"] > 3]\
.groupby("income_category").size())

print(housing.nlargest(10, "rooms_per_household")[["ocean_proximity",
                                             "rooms_per_household",
                                              "median_house_value" ]])


print(housing[(housing["ocean_proximity"] == "NEAR BAY")
               | (housing["ocean_proximity"] == "NEAR OCEAN")]\
.groupby("age_category")["med_income"] \
.mean()
.sort_values(ascending = True))

housing["value_category"] = np.where(
    housing["median_house_value"] > 200000, "expensive", "affordable"
)
print(housing.head())

housing["value_category"] = housing["median_house_value"]\
.apply(lambda x: "expensive" if x > 200000 else "affordable")
print(housing.head(5))


housing["household_size"] = np.where(housing["people_per_household"] > 3, "large", "small")
print(housing.head())

housing["household_size"] = housing["people_per_household"]\
.apply(lambda x: "large" if x > 3 else "small")
print(housing.head())

print(housing.groupby("household_size")["median_house_value"].mean())
conditions = [
    housing["rooms_per_household"] < 4, 
    housing["rooms_per_household"].between(4,6),
    housing["rooms_per_household"] >= 6
]

choices = ["small", "medium", "large"]

housing["room_size"] = np.select(conditions, choices, default = "unknown")
print(housing.head(4))

print(housing.columns.to_list())

# housing1: Location and price info
housing1 = housing[["longitude", "latitude", "ocean_proximity", "median_house_value", "med_income"]].copy()
housing1["house_id"] = range(len(housing1))

# housing2: Size info
housing2 = housing[["total_rooms", "total_bedrooms", "population", "households"]].copy()
housing2["house_id"] = range(len(housing2))

print("housing1 shape:", housing1.shape)
print("housing2 shape:", housing2.shape)
print(housing1.head())
print(housing2.head())

print(pd.merge(housing1, housing2, on = "house_id"))















































