odoo.define('repuestos_stock.repuesto_form', [
    'web.FormController',
    'web.FormView',
    'web.view_registry',
], function (require) {
    'use strict';

    const FormController = require('web.FormController');
    const FormView = require('web.FormView');
    const viewRegistry = require('web.view_registry');

    const RepuestoFormController = FormController.extend({
        _onFieldChanged(event) {
            this._super.apply(this, arguments);

            if (event.data.changes.tipo_repuesto) {
                const tipo = event.data.changes.tipo_repuesto;
                const $form = this.$el;

                console.log('[Repuesto JS] Tipo de repuesto seleccionado:', tipo);

                // Ocultar todas las secciones condicionales
                $form.find('.grupo-inyector, .grupo-frenos, .grupo-sensor').addClass('o_hidden');

                // Mostrar la correspondiente al tipo seleccionado
                if (tipo === 'inyector') {
                    $form.find('.grupo-inyector').removeClass('o_hidden');
                } else if (tipo === 'pastilla') {
                    $form.find('.grupo-frenos').removeClass('o_hidden');
                } else if (tipo === 'sensor') {
                    $form.find('.grupo-sensor').removeClass('o_hidden');
                }
            }
        },
    });

    const RepuestoFormView = FormView.extend({
        config: Object.assign({}, FormView.prototype.config, {
            Controller: RepuestoFormController,
        }),
    });

    viewRegistry.add('repuesto_form_js', RepuestoFormView);
});
