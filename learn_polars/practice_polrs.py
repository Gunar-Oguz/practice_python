import polars as pl
import glob

# ========== FIND ALL FILES ==========
path = "/Users/gulnaralbushova/.cache/kagglehub/datasets/bahramjannesarr/goodreads-book-datasets-10m/versions/18/"

files = glob.glob(f"{path}book*.csv")

# ========== COLUMNS WE NEED (LOWERCASE) ==========
keep_cols = [
    'id',
    'name',
    'authors',
    'rating',
    'pagesnumber',
    'countsofreview',
    'publishyear',
    'language',
    'publisher'
]

# ========== READ EACH FILE, LOWERCASE, KEEP NEEDED ==========
dfs = []
for f in files:
    df = pl.read_csv(f)
    
    df = df\
        .rename({col: col.lower() for col in df.columns})
    
    seen = set()
    unique_cols = []
    for col in df.columns:
        if col not in seen:
            seen.add(col)
            unique_cols.append(col)
    
    df = df\
        .select(unique_cols)
    
    df = df\
        .select(keep_cols)
    
    dfs.append(df)

# ========== STACK ALL FILES ==========
query = pl.concat(dfs)

print("Before cleanup:", 
    query\
        .shape)

# ========== CHECK NULLS ==========
print("\nNull counts:")
print(
    query\
        .null_count()
)

# ========== HANDLE NULLS: pagesnumber ==========
median_pages = query\
    .select(
        pl.col("pagesnumber").median()
    )\
    .item()

print(f"\nMedian pages: {median_pages}")

query = query\
    .with_columns(
        pl.col("pagesnumber").fill_null(median_pages)
    )

# ========== HANDLE NULLS: language (DROP COLUMN) ==========
query = query\
    .drop("language")

print(f"\nColumns after dropping language: {query.columns}")

# ========== HANDLE NULLS: publisher ==========
query = query\
    .with_columns(
        pl.col("publisher").fill_null("Unknown")
    )

# ========== VERIFY NO NULLS ==========
print("\nFinal null check:")
print(
    query\
        .null_count()
)

# ========== CHECK DATA TYPES ==========
print("\nData types:")
print(
    query\
        .schema
)

# ========== CHECK DUPLICATE ROWS ==========
total_rows = query\
    .shape[0]

unique_rows = query\
    .unique()\
    .shape[0]

duplicate_count = total_rows - unique_rows

print(f"\nTotal rows: {total_rows}")
print(f"Duplicate rows: {duplicate_count}")

# ========== REMOVE DUPLICATE ROWS ==========
query = query\
    .unique()

print(f"Rows after removing duplicates: {query.shape[0]}")

# ========== CHECK BOOKS WITH 10K+ REVIEWS ==========
books_10k_reviews = query\
    .filter(pl.col("countsofreview") > 10000)\
    .shape[0]

print(f"\nBooks with 10k+ reviews: {books_10k_reviews}")

# ========== CREATE is_popular FEATURE ==========
query = query\
    .with_columns(
        ((pl.col("rating") > 4.0) & (pl.col("countsofreview") > 10000))\
            .alias("is_popular")
    )

popular_count = query\
    .filter(pl.col("is_popular") == True)\
    .shape[0]

not_popular_count = query\
    .filter(pl.col("is_popular") == False)\
    .shape[0]

print(f"Popular books: {popular_count}")
print(f"Not popular: {not_popular_count}")

# ========== FINAL RESULT ==========
print("\nFinal shape:", 
    query\
        .shape)

print("\nFirst 5 rows:")
print(
    query\
        .head(5)
)

print("Columns:", 
    query\
        .columns)

print(f"Head of the table: ", 
      query\
        .head(2))

print(f"Tail of the table: ", 
      query\
        .tail(2))

print(f"Data types: ",
      query\
        .schema)

print(f"Basic Stat: ", 
      query\
        .describe())

print(f"Unique in publisher: ", 
      query\
        .select(pl.col("publisher").n_unique()))

print(f"Top ten unique publishers: ",
      query\
        .group_by("publisher")\
        .agg(pl.len().alias("count"))\
        .sort("count", descending = True)\
        .head(5))

print(f"Null values: ",
      query\
        .null_count())


print(f"Null percentage: ", 
      query\
        .select(
            (pl.all().null_count() / pl.len() * 100).round(2)
        ))

print(f"Estimaed memory: ", 
      query\
        .estimated_size("mb"), "MB")

print(f"Latest pusblish year: ", 
    query\
        .select(
            pl.col("rating", "pagesnumber", "publishyear").min()
        )
)
print(f"Earlist publish year: ", 
    query\
        .select(
            pl.col("rating", "pagesnumber", "publishyear").max()
        )
)

print(f" Random sample of 10: ", 
    query\
        .sample(n = 10)
)

print(f"Data types: ", 
      query\
        .schema
)

query = query\
    .with_columns(
        pl.col("pagesnumber").cast(pl.Float64)
    )

query = query\
    .with_columns(
        pl.col("id").cast(pl.String)
    )

query = query\
    .with_columns(
        pl.col("pagesnumber").cast(pl.Int64)
    )

query = query\
    .with_columns(
        (pl.col("pagesnumber") > 300).alias("is_long_book")
    )
print(query.head(3))

print(query.columns)












