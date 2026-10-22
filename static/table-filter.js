/**
 * Filtering of the organization tables found on country and topic pages.
 *
 * Beside plain text matching the search supports a platform keyword:
 *
 *     platform:mastodon           organizations with a Mastodon account
 *     platform:facebook,youtube   organizations with a Facebook or a YouTube account
 *     housing platform:mastodon   a platform keyword combined with plain text
 *
 * The search box can also be populated from the URL using a query parameter,
 * ie. /austria/?query=platform:mastodon,peertube
 *
 * The platforms of an organization are read from the data-platforms attribute
 * set by the social icons component.
 */
(function () {
    'use strict';

    var filterInput = document.querySelector('#filter-input');
    var tbody = document.querySelector('tbody');

    if (!filterInput || !tbody) {
        return;
    }

    // "PeerTube" as well as "Peer-Tube" becomes "peertube" so that platforms can
    // be referred to without having to care about casing and punctuation
    function normalize(value) {
        return value.toLowerCase().replace(/[^a-z0-9]/g, '');
    }

    var rows = Array.from(tbody.rows).map(function (row) {
        var platformsElm = row.querySelector('[data-platforms]');
        var platforms = platformsElm ? platformsElm.dataset.platforms.split('|') : [];

        return {
            element: row,
            text: row.textContent.toLowerCase(),
            platforms: platforms.map(normalize).filter(Boolean)
        };
    });

    // splits a query into its plain text part and one list of platforms per
    // platform keyword, ie. "housing platform:mastodon,peertube" becomes
    // { text: 'housing', platformGroups: [['mastodon', 'peertube']] }
    function parseQuery(query) {
        var text = [];
        var platformGroups = [];

        query.trim().split(/\s+/).forEach(function (token) {
            var keyword = /^platform:(.*)$/i.exec(token);

            if (!keyword) {
                text.push(token);
                return;
            }

            var platforms = keyword[1].split(',').map(normalize).filter(Boolean);
            if (platforms.length) {
                platformGroups.push(platforms);
            }
        });

        return { text: text.join(' ').toLowerCase(), platformGroups: platformGroups };
    }

    // every keyword has to match while the platforms of a single keyword are
    // alternatives, platforms match on their beginning so that the table keeps
    // up while a platform name is being typed
    function matchesPlatforms(platforms, platformGroups) {
        return platformGroups.every(function (group) {
            return group.some(function (wanted) {
                return platforms.some(function (platform) {
                    return platform.startsWith(wanted);
                });
            });
        });
    }

    function filter(query) {
        var parsed = parseQuery(query);

        rows.forEach(function (row) {
            var matches = row.text.includes(parsed.text)
                && matchesPlatforms(row.platforms, parsed.platformGroups);
            row.element.style.display = matches ? '' : 'none';
        });
    }

    var query = new URLSearchParams(window.location.search).get('query');
    if (query !== null) {
        filterInput.value = query;
    }

    filterInput.addEventListener('input', function (e) {
        filter(e.target.value);
    });

    // the input may hold a value from the URL or one restored by the browser
    if (filterInput.value) {
        filter(filterInput.value);
    }
})();
