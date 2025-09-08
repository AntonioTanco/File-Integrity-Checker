from Config.json.jsondata import datetime, timezone

def get_sys_utc_time():

    _sys_utc_time = datetime.now(timezone.utc)
    #Returns the current time in UTC for processing

    json_serializable_time = _sys_utc_time.strftime("%Y-%m-%d %H:%M:%S")

    return json_serializable_time

