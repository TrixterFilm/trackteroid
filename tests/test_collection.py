from trackteroid import Query, Asset, AssetVersion


def test_attribute_empty_i4():
    """Tests a bug on the Ftrack API where accessing collection attributes before fetching
    may result on that attribute being "locked": https://github.com/TrixterFilm/trackteroid/issues/4
    """
    asset_collection = Query(Asset).by_id(AssetVersion, "%").get_first()
    assert not asset_collection.versions.id

    asset_collection = Query(Asset).by_id(AssetVersion, "%").get_first(projections=["versions"])
    assert asset_collection.versions.id
