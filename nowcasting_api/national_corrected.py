def get_national_forecast(
    request: Request,
    session: Session = Depends(get_session),
    forecast_horizon_minutes: Optional[int] = None,
    user: Auth0User = Security(get_user()),
    include_metadata: bool = False,
    start_datetime_utc: Optional[str] = None,
    end_datetime_utc: Optional[str] = None,
    creation_limit_utc: Optional[str] = None,
    model_name: ModelEnum = ModelEnum.blend,
) -> Union[NationalForecast, List[NationalForecastValue]]:
    """
    Fetch national forecasts.
    ...
    """
    logger.debug("Get national forecasts")
    ...
