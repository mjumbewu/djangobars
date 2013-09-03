/*globals Backbone Handlebars $ _ */

var DjangobarsSample = DjangobarsSample || {};

(function(NS) {
  // Router ===================================================================
  NS.Router = Backbone.Marionette.AppRouter.extend({
    appRoutes: {
      'page1': 'page1',
      'page2': 'page2',
      '*anything': 'page1'
    }
  });

  NS.controller = {
    page1: function() {
      NS.app.contentRegion.show(new NS.Page1View());
      document.title = Handlebars.templates['page1-title-tpl']();
    },
    page2: function() {
      NS.app.contentRegion.show(new NS.Page2View());
      document.title = Handlebars.templates['page2-title-tpl']();
    }
  };

  // App ======================================================================
  NS.app = new Backbone.Marionette.Application();

  NS.app.addRegions({
    contentRegion: '#content-region',
  });

  // Initializers =============================================================
  NS.app.addInitializer(function(options){
    // Construct a new app router
    this.router = new NS.Router({
      controller: NS.controller
    });

    // Start the router
    Backbone.history.start({ pushState: true, silent: true });

    // Globally capture clicks. If they are internal and not in the pass
    // through list, route them through Backbone's navigate method.
    $(document).on('click', 'a[href^="/"]', function(evt) {
      var $link = $(evt.currentTarget),
          href = $link.attr('href'),
          url;

      evt.preventDefault();

      // Remove leading slashes and hash bangs (backward compatablility)
      url = href.replace(/^\//, '').replace('#!/', '');

      // # Instruct Backbone to trigger routing events
      NS.app.router.navigate(url, {trigger: true});

      return false;
    });
  });

  // Init =====================================================================
  $(function() {
    NS.app.start();
  });

}(DjangobarsSample));