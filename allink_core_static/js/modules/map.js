

export function AMap(pos, title, icon_url) {
    this.initPos = pos;
    this.gmaps = null;
    this.mainloc = null;
    this.title = title;
    this.icon_url = icon_url;
}

AMap.prototype.init = function() {
    this.gmaps = new google.maps.Map(document.getElementById('gmaps'), {
        center: this.initPos,
        zoom: 18,
        scrollwheel: false,
        mapTypeId: google.maps.MapTypeId.HYBRID,
        streetViewControl: false,
        tilt: 0
    });

    var m_options = {
        position: this.initPos,
        map: this.gmaps,
        title: this.title,
    };

    if (this.icon_url) {
        m_options.icon = {
            url: this.icon_url,
            size: new google.maps.Size(40, 59),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(20, 59)
        };
    }

    this.mainloc = new google.maps.Marker(m_options);

    for(var i = 0; i < window.SUBLOCS.length; i++) {
        var loc = window.SUBLOCS[i];
        this.addSubLocation(loc);
    }
};

AMap.prototype.addSubLocation = function(options) {
    var img = {
        url: options.icon,
        size: new google.maps.Size(33, 53),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(16, 53)
    };

    var marker = new google.maps.Marker({
        position: options.pos,
        map: this.gmaps,
        title: options.title,
        icon: img,
    });
};

export const initMap = function () {
    var styles = [
        {
            "featureType":"water",
            "elementType":"geometry.fill",
            "stylers":[{"color":"#d3d3d3"}]
        },{
            "featureType":"transit",
            "stylers":[{"color":"#808080"},{"visibility":"off"}]
        },{
            "featureType":"road.highway",
            "elementType":"geometry.stroke",
            "stylers":[{"visibility":"on"},{"color":"#b3b3b3"}]
        },{
            "featureType":"road.highway","elementType":"geometry.fill","stylers":[
            {"color":"#ffffff"}
            ]
        },{
            "featureType":"road.local","elementType":"geometry.fill","stylers":[
            {"visibility":"on"},{"color":"#ffffff"},{"weight":1.8}]
        },{
            "featureType":"road.local","elementType":"geometry.stroke","stylers":[{"color":"#d7d7d7"}]
        },{
            "featureType":"poi","elementType":"geometry.fill","stylers":[{"visibility":"on"},{"color":"#ebebeb"}]
        },{
            "featureType":"administrative","elementType":"geometry","stylers":[{"color":"#a7a7a7"}]
        },{
            "featureType":"road.arterial","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]
        },{
            "featureType":"road.arterial","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]
        },{
            "featureType":"landscape","elementType":"geometry.fill","stylers":[{"visibility":"on"},{"color":"#efefef"}]
        },{
            "featureType":"road","elementType":"labels.text.fill","stylers":[{"color":"#696969"}]
        },{
            "featureType":"administrative","elementType":"labels.text.fill","stylers":[{"visibility":"on"},{"color":"#737373"}]
        },{
            "featureType":"poi","elementType":"labels.icon","stylers":[{"visibility":"off"}]
        },{
            "featureType":"poi","elementType":"labels","stylers":[{"visibility":"off"}]
        },{
            "featureType":"road.arterial","elementType":"geometry.stroke","stylers":[{"color":"#d6d6d6"}]
        },{
            "featureType":"road","elementType":"labels.icon","stylers":[{"visibility":"off"}]
        },{
            "featureType":"poi","elementType":"geometry.fill","stylers":[{"color":"#dadada"}]
        },{
            "featureType":"landscape.natural","elementType":"labels","stylers":[{"visibility":"off"}]
        }

    ];

    function createMarker(markerPos,infowindow_content,map) {
        var pin = {

            url: '/static/images/pin3.png',
            size: new google.maps.Size(28, 40), // half the actual size (squeezed), otherwise the info window is not centered correctly
            scaledSize: new google.maps.Size(28, 40),
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(14, 40)

            // SVG path positioning wasn't working, so let's postpone this one
            // path: 'M7,0C3.1,0,0,3.1,0,7c0,5.2,7,13,7,13s7-7.8,7-13C14,3.1,10.9,0,7,0z M7,9.5C5.6,9.5,4.5,8.4,4.5,7S5.6,4.5,7,4.5 S9.5,5.6,9.5,7S8.4,9.5,7,9.5z',
            // fillColor: '#1e42ab',
            // fillOpacity: 1,
            // scale: 1, // this results in 28x40 pixel
            // strokeWeight: 0,
            // This marker is 20 pixels wide by 32 pixels high.
            // size: new google.maps.Size(28, 40),
            // The origin for this image is (0, 0).
            // origin: new google.maps.Point(0,0),
            // The anchor for this image is the base of the flagpole at (0, 32).
            // anchor: new google.maps.Point(14, 20),
          };

        var marker = new google.maps.Marker({
          position: markerPos,
          map: map,
          icon: pin,
          info: infowindow_content,
        });

        return marker;
    }

    var mapCanvas = document.getElementById('map-canvas');

    window.initMap = () => {

        var mapOptions = {
            zoom: 16,
            streetViewControl: false,
            mapTypeControl: false,
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            mapTypeControlOptions: {
                mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
            }
        };

        var styledMap = new google.maps.StyledMapType(styles,{name: "Styled Map"});
        var map = new google.maps.Map(mapCanvas, mapOptions);
        var bounds = new google.maps.LatLngBounds();
        var infoWindow = new google.maps.InfoWindow({
            content: 'Loading...',
            // pixelOffset: 50,
          });
        map.mapTypes.set('map_style', styledMap);
        map.setMapTypeId('map_style');

        for (var i = window.MAP_LOCATIONS.length - 1; i >= 0; i--) {

            var lat = parseFloat(window.MAP_LOCATIONS[i].lat.replace(',', '.'));
            var lng = parseFloat(window.MAP_LOCATIONS[i].lng.replace(',', '.'));
            var infowindow_content = window.MAP_LOCATIONS[i].infowindow_content;

            var markerPos = new google.maps.LatLng(lat,lng);

            var marker = createMarker(markerPos,infowindow_content,map);

            // extend map boundaries
            bounds.extend(markerPos);

            // Automatically center the map fitting all markers on the screen
            map.fitBounds(bounds);

            // fill info box with individual content
            marker.addListener('click', function() {
                infoWindow.setContent( this.info );
                infoWindow.open(map, this);
            });

        }

        google.maps.event.addDomListener(window, 'resize', function() {
            map.fitBounds(bounds);
        });

    };

    if(mapCanvas) {
        // TBD: limit URL to final domain in Google Console
        // load google maps api
        let google_maps_script = document.createElement('script');
        google_maps_script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBICVW4AeweLqunuGb1ibiESjbGSbPg6Aw&callback=initMap';
        document.body.appendChild(google_maps_script);
    }
};
