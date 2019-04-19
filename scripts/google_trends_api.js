/*
 * This Source Code Form is subject to the terms of the MIT
 * License. If a copy of the same was not distributed with this
 * file, You can obtain one at
 * https://github.com/akhilpandey95/altpred/blob/master/LICENSE.
*/

const trends = require('google-trends-api');

/*
 * function for getting interest over time for a keyword
 *
 * @param (string) - keyword
 * @param (date)   - start date from where search should start
 * @param (date)   - end date to where the search must end
 *
*/
module.exports.get_interest_over_time = (keyword, start, end) => {
    // make the request for getting the trends over time
    trends.interestOverTime({keyword: keyword, startTime: start, endTime: end})
        .then(function(results) {
            return results;
        })
        .catch(function(err) {
            return err;
        });
}

/*
 * function for getting related topics for a certain keyword
 *
 * @param (string) - keyword
 * @param (date)   - start date from where search should start
 * @param (date)   - end date to where the search must end
 *
*/
module.exports.get_related_topics = (keyword, start, end) => {
    // make the request for getting related topics for a keyword over time
    trends.relatedTopics({keyword: keyword, startTime: start, endTime: end})
        .then(function(results) {
            return results;
        })
        .catch(function(err) {
            return err;
        });
}

