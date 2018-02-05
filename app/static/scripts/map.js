function start() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(initMaps);
    } 
    {% block script %} {% endblock %}
    function initMaps(position) {
        var directionsDisplay = new google.maps.DirectionsRenderer;
        var directionsService = new google.maps.DirectionsService;
        var latlong = position.coords.latitude + "," + position.coords.longitude;
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 16,
            center: {
                lat: 33.881994,
                lng: -117.885076
            },
            streetViewControl: false,
            mapTypeControl: false,
            styles: [{
                    "featureType": "landscape",
                    "stylers": [{
                            "hue": "#FFA800"
                        },
                        {
                            "saturation": 0
                        },
                        {
                            "lightness": 0
                        },
                        {
                            "gamma": 1
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "stylers": [{
                            "hue": "#53FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": 40
                        },
                        {
                            "gamma": 1
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "stylers": [{
                            "hue": "#FBFF00"
                        },
                        {
                            "saturation": 0
                        },
                        {
                            "lightness": 0
                        },
                        {
                            "gamma": 1
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "geometry",
                    "stylers": [{
                            "hue": "#FFFFFF"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": 100
                        },
                        {
                            "gamma": 1
                        }
                    ]
                },
                {
                    "featureType": "water",
                    "stylers": [{
                            "hue": "#00BFFF"
                        },
                        {
                            "saturation": 6
                        },
                        {
                            "lightness": 8
                        },
                        {
                            "gamma": 1
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "stylers": [{
                            "hue": "#679714"
                        },
                        {
                            "saturation": 33.4
                        },
                        {
                            "lightness": -25.4
                        },
                        {
                            "gamma": 1
                        }
                    ]
                }
            ]
        });
        directionsDisplay.setMap(map);
        var control = document.getElementById('floating-panel');
        control.style.display = 'block';
        // display the customized icons
        // add any needed icons using the below format in var icons
        var icons = {
            parking: {
                name: 'Parking',
                icon: 'https://newcdn.iconfinder.com/data/icons/rental-icon/240/parking-20.png'
            },
            library: {
                name: 'Library',
                icon: 'https://cdn0.iconfinder.com/data/icons/octicons/1024/book-20.png'
            },
            titan_student_union: {
                name: 'Titan Student Union',
                icon: 'https://newcdn.iconfinder.com/data/icons/pittogrammi/142/97-20.png'
            },
            book_store: {
                name: 'Book Store',
                icon: 'https://cdn4.iconfinder.com/data/icons/essential-app-1/16/shopping-bag-paper-store-20.png'
            }
        };
        // array of icons to be used on the map.
        var features = [{
            position: new google.maps.LatLng(33.880303, -117.881738),
            type: 'parking'
        }, {
            position: new google.maps.LatLng(33.883071, -117.888595),
            type: 'parking'
        }, {
            position: new google.maps.LatLng(33.884843, -117.889426),
            type: 'parking'
        }, {
            position: new google.maps.LatLng(33.879039, -117.888448),
            type: 'parking'
        }, {
            position: new google.maps.LatLng(33.883071, -117.888595),
            type: 'parking'
        }, {
            position: new google.maps.LatLng(33.881101, -117.885359),
            type: 'library'
        }, {
            position: new google.maps.LatLng(33.881402, -117.887644),
            type: 'titan_student_union'
        }, {
            position: new google.maps.LatLng(33.881897, -117.886883),
            type: 'book_store'
        }];
        // put the markers on the map
        features.forEach(function(feature) {
            var marker = new google.maps.Marker({
                position: feature.position,
                icon: icons[feature.type].icon,
                map: map
            });
        });
        document.getElementById('location').value = latlong; 
        {% block call %} {% endblock %}
    }
}
