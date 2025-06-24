
odoo.define
(
    'repuestos_stock.repuesto_form', ['web.FormController', 'web.FormView', 'web.view_registry'], function (require) 
    {
        'use strict';

        const FormController = require('web.FormController');
        const FormView = require('web.FormView');
        const viewRegistry = require('web.view_registry');

        const RepuestoFormController = FormController.extend({
            _onFieldChanged: function (event) {
                this._super.apply(this, arguments);
                if (event.data.changes.hasOwnProperty('tipo_repuesto')) {
                    const tipo = event.data.changes.tipo_repuesto;
                    const $grupoInyector = this.$('.inyector-section');

                    if (tipo === 'inyector') {
                        $grupoInyector.removeClass('o_hidden');
                    } else {
                        $grupoInyector.addClass('o_hidden');
                    }
                }
            }
        });

        const RepuestoFormView = FormView.extend({
            config: _.extend({}, FormView.prototype.config, {
                Controller: RepuestoFormController,
            }),
        });

        viewRegistry.add('repuesto_form_js', RepuestoFormView);
    }
);
