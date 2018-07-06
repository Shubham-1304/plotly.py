import _plotly_utils.basevalidators


class ScaleratioValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='scaleratio', parent_name='layout.yaxis', **kwargs
    ):
        super(ScaleratioValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            min=0,
            role='info',
            **kwargs
        )