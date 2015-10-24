from django import template

register = template.Library()


@register.simple_tag
def dynamicform_js():
    return  '''
<script type="text/javascript">
  $('form.dynamic-form button.validate-button').click(function(e) {
    var $form = $(e).parent('form');
    $.ajax({
      url: $form.attr('action'),
      type: "GET",
      data: $form.serialize(),
      success: function(data) {
        $('.dynamic-form .error-container').text('');
        if (typeof data.errors !== 'undefined' && data.errors) {
          var errors = data.errors;
          for (var key in errors) {
            var $errorInput = $('input[name=' + key + ']');
            var $errorContainer = $('#form_error_' + $errorInput.attr('id'));
            $errorContainer.text(errors[key]);
          }
        }
        // TODO: Allow user to specify a callback.
      }
    });
    e.preventDefault();
  });

  $('.ajax-validate').blur(function(e) {
    var element = e.target;
    var $form = $('form')[0];

    $.ajax({
      url: $form.action + '?validate=' + element.name + '&' + element.name + '=' + element.value,
      success: function(data) {
        var $errorContainer = $('#form_error_' + element.id);
        if (typeof data.error !== 'undefined' && data.error) {
          $errorContainer.text(data.error);
        } else {
          $errorContainer.text('');
        }
      }
    });
  });
</script>
'''
