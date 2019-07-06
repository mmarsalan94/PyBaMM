#
# Lithium ion bulter-volmer class
#

from .base_bulter_volmer import BaseModel


class LithiumIon(BaseModel):
    """
    Lithium-ion Butler-Volmer class

    **Extends:** :class:`pybamm.interface.butler_volmer.BaseModel`
    """

    def __init__(self, param, domain):
        super().__init__(param, domain)

    def _get_exchange_current_density(self, variables):
        """
        A private function to obtain the exchange current density for a lithium-ion
        intercalation reaction.

        Parameters
        ----------
        variables: dict
        `   The variables in the full model.

        Returns
        -------
        j0 : :class: `pybamm.Symbol`
            The exchange current density.
        """

        c_s_surf = variables[self.domain + " particle surface concentration"]
        c_e = variables[self.domain + " electrolyte concentration"]

        if self.domain == "Negative":
            prefactor = 1 / self.param.C_r_n
        elif self.domain == "Positive":
            prefactor = self.param.gamma_p / self.param.C_r_p

        j0 = prefactor * (
            c_e ** (1 / 2) * c_s_surf ** (1 / 2) * (1 - c_s_surf) ** (1 / 2)
        )

        return j0