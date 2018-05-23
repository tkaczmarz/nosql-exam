if __name__ == "__main__":
    import os

    os.system(
        "mongoimport --host mongodb_database --port 27017 -d test -c crimes --type csv --file /tmp/Chicago_Crimes_2001_to_2004.csv --headerline && rm /tmp/crimes.zip")
    from . import make_plots, crimes_aggr, crimes_mr, not_arrested, app
    crimes_mr.map_reduce("mongodb_database")
    crimes_aggr.aggregattion("mongodb_database")
    not_arrested.not_arrested("mongodb_database")
    make_plots.generate_charts()
    app.start()
