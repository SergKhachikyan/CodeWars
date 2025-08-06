def was_package_received_yesterday(tz_from, tz_to, start, duration):
    utc_departure = start - tz_from
    utc_arrival = utc_departure + duration

    local_arrival = utc_arrival + tz_to

    return local_arrival < 0
