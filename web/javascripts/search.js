// Create namespace ------------------------------------------------------------
if (at == undefined) var at = {};
if (at.bartelme == undefined) at.bartelme = {};

/**
 * Mac OS Search Field
 * Replaces the default input field with the typical Mac OS search field
 * 
 * Copyright 2006 Wolfgang Bartelme
 * Bartelme Design - http://bartelme.at
 */

// Search Field class ----------------------------------------------------------
at.bartelme.searchField = Class.create();
at.bartelme.searchField.prototype = {
  initialize: function()
  {
    this.search_field  = $("quicksearch_field");
    this.default_value = this.search_field.getAttribute('title'); //"search this site...";
    this.is_safari     = ((parseInt(navigator.productSub)>=20020000)&&(navigator.vendor.indexOf("Apple Computer")!=-1));
    if (this.is_safari) {
      Element.addClassName(this.search_field, "issafari");
      this.replace();      
    } else {
      if (this.search_field.value == "") this.search_field.value = this.default_value;
    }
    Event.observe(this.search_field, "focus", this.focus.bindAsEventListener(this), false);
    Event.observe(this.search_field, "blur",  this.blur.bindAsEventListener(this),  false);
  },
  replace: function()
  {
    this.search_field.setAttribute('type', 'search');
    this.search_field.setAttribute('autosave', 'ee.arx.search');
    this.search_field.setAttribute('results', '5');
    this.search_field.setAttribute('placeholder', this.default_value);
  },
  focus: function()
  {
    if (this.search_field.value == this.default_value) {
      this.search_field.value = "";
      Element.addClassName(this.search_field, "focus");
    }
  },
  blur: function()
  {
    if (this.search_field.value == "") {
      if (this.is_safari) {
        this.search_field.value = "";        
      } else {
        this.search_field.value = this.default_value;
        Element.removeClassName(this.search_field, "focus");
      }
    }
  }
}

Event.observe(window, "load", function(){new at.bartelme.searchField()}, false);