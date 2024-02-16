// ignore_for_file: non_constant_identifier_names

import 'dart:async';

import 'package:geolocator/geolocator.dart';
import 'package:here_final/features/map/map_controller.dart';
import 'package:here_sdk/core.dart';
import 'package:here_sdk/core.errors.dart';
import 'package:here_sdk/search.dart';

class Searching {
  SearchEngine? _searchEngine;
  MapController mapController = MapController();

  Searching() {
    try {
      _searchEngine = SearchEngine();
    } on InstantiationException {
      throw Exception("Initialization of SearchEngine failed.");
    }
  }

  Future<List<GeoCoordinates>> getPlaces({
    required PlaceCategory categoryList,
    required GeoCoordinates geoCoordinates,
  }) async {
    Completer<List<GeoCoordinates>> completer =
        Completer<List<GeoCoordinates>>();
    final GeoCoordinates cP = await mapController.getPermisson();
    var queryArea = CategoryQueryArea.withCenter(cP);
    CategoryQuery categoryQuery = CategoryQuery.withCategoriesInArea(
      [categoryList],
      queryArea,
    );

    SearchOptions searchOptions = SearchOptions();
    searchOptions.languageCode = LanguageCode.enUs;
    searchOptions.maxItems = 20;

    List<GeoCoordinates> geo = [];
    _searchEngine!.searchByCategory(categoryQuery, searchOptions,
        (SearchError? searchError, List<Place>? list) async {
      if (searchError != null) {
        completer.completeError(
            searchError); // Complete with an error if there's an issue.
        return;
      }

      for (Place searchResult in list!) {
        geo.add(searchResult.geoCoordinates!);
      }

      completer.complete(
          geo); // Complete with the result when the operation is done.
    });

    return completer.future;
  }
}
