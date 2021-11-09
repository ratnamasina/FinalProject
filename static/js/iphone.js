$("select.positionTypes").change(function () {
    $("select option[value='" + $(this).data('index') + "']").prop('disabled', false);
    $(this).data('index', this.value);
    $("select option[value='" + this.value + "']:not([value=''])").prop('disabled', true);
    });