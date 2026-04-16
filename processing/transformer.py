from decorator.timer_decorator import timer

@timer  # decorator ensures how long my transformation takes 
def transform_data(data):

    data = data.copy()

    data.columns = [col.lower() for col in data.columns]

    data.loc[:, "name"] = data["name"].str.lower()

    data.loc[:, "salary_category"] = data["salary"].apply(
        lambda x: "Low" if x < 50000 else "Medium" if x < 60000 else "High"
    )

    return data