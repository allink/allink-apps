const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');

// const CopyWebpackPlugin = require('copy-webpack-plugin');
// const BUILD_FOLDER = path.join(__dirname, 'static/build/');

exports.production = function() {
    return {
        output: {
        	filename: '[name].min.[hash].js'
        },
        plugins: [
            new BundleTracker({filename: './webpack-stats.json'}),
            new webpack.optimize.UglifyJsPlugin({
                compress: {
                    warnings: false,
                },
                output: {
                    comments: false,
                },
            }),
            new ExtractTextPlugin('[name].min.[hash].css'),
            // new CopyWebpackPlugin([
            //     {
            //         from: path.join(BUILD_FOLDER, 'djangocms*.css'),
            //         to: path.join(BUILD_FOLDER, 'test.css'),
            //     },
            //     {
            //         copyUnmodified: true,
            //     },
            // ]),
        ]
    };
};

exports.development = function() {
    return {
        output: {
            filename: '[name].js'
        },
        plugins: [
            new BundleTracker({filename: './webpack-stats.json'}),
            new ExtractTextPlugin('[name].css'),
        ]
    };
};
