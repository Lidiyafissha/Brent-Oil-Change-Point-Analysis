import numpy as np
import pymc as pm


def fit_mean_change_point_model(returns, draws=10, tune=10):
    """
    Fits a Bayesian change point model with a mean shift.

    Parameters
    ----------
    returns : np.ndarray
        Stationary time series (e.g. log returns)
    draws : int
        Number of posterior samples
    tune : int
        Number of tuning steps

    Returns
    -------
    model : pm.Model
    trace : arviz.InferenceData
    """

    if len(returns) < 30:
        raise ValueError("Time series too short for change point modeling.")

    returns = np.asarray(returns)
    n = len(returns)
    time_idx = np.arange(n)

    with pm.Model() as model:
        tau = pm.DiscreteUniform("tau", lower=0, upper=n - 1)

        mu_1 = pm.Normal("mu_1", mu=0, sigma=1)
        mu_2 = pm.Normal("mu_2", mu=0, sigma=1)

        sigma = pm.HalfNormal("sigma", sigma=1)

        mu = pm.math.switch(time_idx <= tau, mu_1, mu_2)

        pm.Normal("obs", mu=mu, sigma=sigma, observed=returns)

        trace = pm.sample(
            draws=draws,
            tune=tune,
            target_accept=0.9,
            return_inferencedata=True,
            progressbar=True
        )

    return model, trace
