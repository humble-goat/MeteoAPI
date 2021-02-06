if __name__ == '__main__':

    import user
    from tools import print_data
    from weather import get_forecast, Flag

    local_user = user.LocalUser
    local_user.initialize_user()
    location = local_user.get_location()
    data = get_forecast(location.latitude, location.longitude, Flag.HOURLY)
    currently = get_forecast(location.latitude, location.longitude, Flag.CURRENTLY)
    details = get_forecast(location.latitude, location.longitude, Flag.DAY_DETAILS, '2021-02-08')
    print_data(details)
