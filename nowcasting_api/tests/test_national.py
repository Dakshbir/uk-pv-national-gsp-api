def test_get_national_forecast_with_model_name(db_session, api_client):
    """Check main solar/GB/national/forecast route works with different model names"""

    models = ["blend", "pvnet_v2", "pvnet_da", "pvnet_ecwmf"]
    
    for model_name in models:
        model = get_model(db_session, name=model_name, version="0.0.1")

        forecast = make_fake_national_forecast(
            session=db_session, t0_datetime_utc=datetime.now(tz=timezone.utc)
        )
        forecast.model = model

        db_session.add(forecast)
        update_all_forecast_latest(forecasts=[forecast], session=db_session)

        app.dependency_overrides[get_session] = lambda: db_session

        response = api_client.get(f"/v0/solar/GB/national/forecast?model_name={model_name}")
        assert response.status_code == 200

        national_forecast_values = [NationalForecastValue(**f) for f in response.json()]
        assert national_forecast_values[0].plevels is not None
        assert len(national_forecast_values) > 0  # Ensure we get some forecast values
