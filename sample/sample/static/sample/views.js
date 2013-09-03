/*globals Backbone Handlebars $ _ */

var DjangobarsSample = DjangobarsSample || {};

(function(NS) {

  // Templates ================================================================
  //
  // Replace the compileTemplate method to compile our Handlebars templates 
  // instead of using Underscore templates.
  Backbone.Marionette.TemplateCache.prototype.compileTemplate = function(rawTemplate) {
    return Handlebars.compile(rawTemplate);
  };

  // Views ====================================================================
  NS.Page1View = Backbone.Marionette.ItemView.extend({
    template: '#page1-tpl',
  });

  NS.Page2View = Backbone.Marionette.ItemView.extend({
    template: '#page2-tpl',
  });

}(DjangobarsSample));