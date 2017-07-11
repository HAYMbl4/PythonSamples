const willGoProgressId = "will-go-progress";
const wontGoProgressId = "wont-go-progress";
const maybeGoProgressId = "maybe-go-progress";
const visitorsCount = 100;

$(document).ready(function () {

    var url = "/cgi-bin/get_statistic.py";

    $.ajax({
        type: "get",
        url: url,
        dataType: "json",
        success: function (data) {
            fillCommonStatistic(data.visitors);
            fillTransferStatistic(data.transferStatistic);
            fillEventsStatistic(data.eventsStatistic);
            fillDrinksStatistic(data.drinksStatistic);
            fillMainMealStatistic(data.mainMealStatistic);
            fillWillGoProgress(data.willGoStatistic, data.visitors.length);
            $('[data-toggle="popover"]').popover();
        }
    });
});

function fillCommonStatistic(visitors) {
    for (var i = 0; i < visitors.length; i++) {
        addCommonStatisticRow("visitors-table", visitors[i]);
    }
}

function fillTransferStatistic(transferStatistic) {
    for (var i = 0; i < transferStatistic.length; i++) {
        addStatisticRow("transfer-table", transferStatistic[i])
    }
}

function fillEventsStatistic(eventsStatistic) {
    for (var i = 0; i < eventsStatistic.length; i++) {
        addStatisticRow("events-table", eventsStatistic[i])
    }
}

function fillDrinksStatistic(drinksStatistic) {
    for (var i = 0; i < drinksStatistic.length; i++) {
        addStatisticRow("drinks-table", drinksStatistic[i])
    }
}

function fillMainMealStatistic(mainMealStatistic) {
    for (var i = 0; i < mainMealStatistic.length; i++) {
        addStatisticRow("main-meal-table", mainMealStatistic[i])
    }
}

function fillWillGoProgress(willGoStatistic, rowCount) {
    var allCount = Math.abs(visitorsCount - rowCount);

    if (visitorsCount !== 0) {
        fillPartOfProgress(maybeGoProgressId, visitorsCount, visitorsCount - rowCount, " (думают)");
        allCount = visitorsCount;
    }

    for (var i = 0; i < willGoStatistic.length; i++) {
        var count = willGoStatistic[i].persons.length;

        if (willGoStatistic[i].position) {
            fillPartOfProgress(willGoProgressId, allCount, count, " (идут)");
        } else {
            fillPartOfProgress(wontGoProgressId, allCount, count, " (не идут)");
        }
    }
}

function fillPartOfProgress(divId, allCount, count, description) {
    get(divId).attr("aria-valuenow", count);
    get(divId).css({"width": calculatePercents(allCount, count) + "%"});
    get(divId).text(count + description);
}

function calculatePercents(all, part) {
    return (part * 100) / all;
}

function addCommonStatisticRow(tableId, obj) {
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

function addStatisticRow(tableId, obj) {
    var row =
        "<tr><td>" + obj.position +
        "</td><td>" + obj.persons.length +
        "</td><td>" + getPersonsListPopover(obj.persons) +
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

function getPersonsListPopover(persons) {
    return "<a href='#' data-toggle='popover' data-container='body' data-placement='bottom' data-content='" + persons + "'> " +
        "   <i class='fa fa-group text-gray-dark'></i> " +
        "</a>";
}

function popoverOptions() {
    $('[data-toggle="popover"]').popover();
}