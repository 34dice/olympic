# olympic_medal_count.py

# Sample data

datset = []
data = {
    "Country": ["USA", "China", "Japan", "Germany", "Russia"],
    "Gold": [39, 38, 27, 10, 20],
    "Silver": [41, 32, 14, 11, 28],
    "Bronze": [33, 18, 17, 16, 23]
}
print(data)

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to calculate the total number of medals for each country
def calculate_total_medals(df):
    df["Total"] = df["Gold"] + df["Silver"] + df["Bronze"]
    return df

# Function to display the sorted medal count
def display_medal_count(df):
    print("\nOlympic Medal Count:")
    print(df.sort_values(by="Total", ascending=False))

# Main function to run the script
def main():
    print("Welcome to the Olympic Medal Count Analysis")
    
    # Calculate total medals and display the results
    df_with_totals = calculate_total_medals(df)
    display_medal_count(df_with_totals)

    # Save the result to a CSV file
    df_with_totals.to_csv("olympic_medal_count.csv", index=False)
    print("\nData saved to 'olympic_medal_count.csv'.")

# Run the main function if executed directly
if __name__ == "__main__":
    main()
