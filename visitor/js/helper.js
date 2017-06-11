function toBoolean(value) {
    switch (value.toLowerCase().trim()) {
        case "1":
        case "true":
            return true;
        case "0":
        case "false":
            return false;
    }
}

function get(elementId) {
    return $("#" + elementId);
}

function getValue(elementId) {
    return get(elementId).val();
}

function getChoseItems(elementId) {
    var items = [];
    get(elementId).find(":selected").each(function (i, selected) {
        items[i] = $(selected).text();
    });
    return items;
}

function writeLikeList(items) {
    var text = "";
    for (var i = 0; i < items.length; i++) {
        text += items[i] + "<br/>";
    }
    return text;
}

function toggleWarnIndicator(element, hasWarning) {
    if (hasWarning) {
        element.addClass("form-control-warning");
        element.parent().addClass("has-warning");
    } else {
        element.removeClass("form-control-warning");
        element.parent().removeClass("has-warning");
    }
}

function checkStringValue(value) {
    return value.trim() === "";
}

function checkArrayValue(value) {
    return value.length === 0;
}

function checkValue(element) {
    var value = element.val();
    var hasError = false;

    if (typeof value === "string" || value instanceof String) {
        hasError = checkStringValue(value);
    } else if (value instanceof Array) {
        hasError = checkArrayValue(value);
    }

    toggleWarnIndicator(element, hasError);
    return hasError;
}