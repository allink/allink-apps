const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');
const path = require('path');

exports.production = function() {
    return {
        output: {
            // filename: '[name].min.[hash].js'
            filename: '[name].js'
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
            // new ExtractTextPlugin('[name].min.[hash].css'),
            new ExtractTextPlugin('[name].css'),
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
            // new webpack.optimize.UglifyJsPlugin({
            //     compress: {
            //         warnings: false,
            //     },
            //     output: {
            //         comments: false,
            //     },
            // }),
            new ExtractTextPlugin('[name].css'),
        ]
    };
};
