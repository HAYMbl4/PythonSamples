const willGoFormId = "will-go-form";
const willGoTableId = "will-go-table";
const willGoInfoPanelId = "will-go-info-panel";
const willGoButtonsId = "will-go-buttons";

const willGoElementId = "will-go";
const wontGoElementId = "wont-go";
const nameElementId = "name";
const transferElementId = "transfer";
const eventsElementId = "events";
const drinksElementId = "drinks";
const mainMealElementId = "main-meal";
const noteElementId = "note";

var visitors = [];

$(document).ready(function () {
    get(willGoFormId).submit(function (e) {
        e.preventDefault();
    });
});

function saveAndSendWillGoInfo() {
    var url = "/cgi-bin/will_go.py";

    $.ajax({
        type: "post",
        url: url,
        data: "visitors=" + JSON.stringify(visitors),
        dataType: "json",
        success: function (data) {
            if (toBoolean(data["success"])) {
                if (data["positive_desc"] !== null) {
                    get("will-go-response").text(data["positive_desc"]);
                    get("will-go-response").removeClass("hide");
                    setTimeout(function () {
                        get("will-go-response").addClass("hide");
                    }, 5000);
                }
                if (data["negative_desc"] !== null) {
                    get("wont-go-response").text(data["negative_desc"]);
                    get("wont-go-response").removeClass("hide");
                    setTimeout(function () {
                        get("wont-go-response").addClass("hide");
                    }, 5000);
                }
            } else {
                get("error-response").text("Ошибка при обработке: " + data["exp"]);
                get("error-response").removeClass("hide");
            }
        }
    });
}

function addVisitor() {
    if (!checkWillGoForm()) {
        var visitor = createVisitor();
        visitors.push(visitor);
        addVisitorRow(willGoTableId, visitor);
        resetWillGoForm(willGoFormId);
        onToggleWillGo();
    }
    showOrHideTable();
}

function sendVisitors() {
    if (visitors.length !== 0) {
        saveAndSendWillGoInfo();
        onToggleWillGo();
    } else if (!checkWillGoForm()) {
        visitors.push(createVisitor());
        saveAndSendWillGoInfo();
        resetWillGoForm(willGoFormId);
        onToggleWillGo();
    }
    visitors = [];
    showOrHideTable();
}

function checkWillGoForm() {
    var hasErrors = false;

    if (checkValue(get(nameElementId))) {
        hasErrors = true;
    }

    if (toBoolean(getWillGoElement().value)) {
        if (checkValue(get(transferElementId))) {
            hasErrors = true;
        }
        if (checkValue(get(eventsElementId))) {
            hasErrors = true;
        }
        if (checkValue(get(drinksElementId))) {
            hasErrors = true;
        }
        if (checkValue(get(mainMealElementId))) {
            hasErrors = true;
        }
    }

    return hasErrors;
}

function createVisitor() {
    var visitor = {};

    visitor.name = getValue(nameElementId);
    visitor.willGo = toBoolean(getWillGoElement().value);
    visitor.transfer = getValue(transferElementId);
    visitor.events = getChoseItems(eventsElementId);
    visitor.drinks = getChoseItems(drinksElementId);
    visitor.mainMeal = getValue(mainMealElementId);
    visitor.note = getValue(noteElementId);

    return visitor;
}

function onToggleWillGo() {
    var willGo = toBoolean(getWillGoElement().value);
    var willGoInfoPanel = get(willGoInfoPanelId);
    willGo ? willGoInfoPanel.removeClass("hide") : willGoInfoPanel.addClass("hide");
}

function getWillGoElement() {
    return get(willGoButtonsId).find("input:radio:checked")[0];
}

function showOrHideTable() {
    visitors.length === 0 ? get(willGoTableId).addClass("hide") : get(willGoTableId).removeClass("hide");
}

function resetWillGoForm(formId) {
    get(formId)[0].reset();
    get(eventsElementId).multiselect("refresh");
    get(drinksElementId).multiselect("refresh");
    get(willGoElementId).parent().addClass("active");
    get(wontGoElementId).parent().removeClass("active");
}

function addVisitorRow(tableId, obj) {
    var row =
        "<tr><td>" + getWillGoIconHtml(obj.willGo) + obj.name +
        "</td><td>" + obj.transfer +
        "</td><td>" + writeLikeList(obj.events) +
        "</td><td class='hidden-sm-down'>" + writeLikeList(obj.drinks) +
        "</td><td class='hidden-sm-down'>" + obj.mainMeal +
        "</td><td class='hidden-sm-down'>" + obj.note +
        "</td></tr>";

    get(tableId).append(row);
}

function getWillGoIconHtml(willGo) {
    if (willGo) {
        return "<i class='fa fa-check text-success pr-2'></i>";
    } else {
        return "<i class='fa fa-close text-danger pr-2'></i>";
    }
}