"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
self["webpackHotUpdate_N_E"]("app/layout",{

/***/ "(app-pages-browser)/./app/globals.css":
/*!*************************!*\
  !*** ./app/globals.css ***!
  \*************************/
/***/ (function(module, __webpack_exports__, __webpack_require__) {

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony default export */ __webpack_exports__[\"default\"] = (\"01f5f15a954f\");\nif (true) { module.hot.accept() }\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL2FwcC9nbG9iYWxzLmNzcyIsIm1hcHBpbmdzIjoiO0FBQUEsK0RBQWUsY0FBYztBQUM3QixJQUFJLElBQVUsSUFBSSxpQkFBaUIiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9fTl9FLy4vYXBwL2dsb2JhbHMuY3NzPzQ4NDYiXSwic291cmNlc0NvbnRlbnQiOlsiZXhwb3J0IGRlZmF1bHQgXCIwMWY1ZjE1YTk1NGZcIlxuaWYgKG1vZHVsZS5ob3QpIHsgbW9kdWxlLmhvdC5hY2NlcHQoKSB9XG4iXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///(app-pages-browser)/./app/globals.css\n"));

/***/ }),

/***/ "(app-pages-browser)/./app/contexts/StateContext.tsx":
/*!***************************************!*\
  !*** ./app/contexts/StateContext.tsx ***!
  \***************************************/
/***/ (function(module, __webpack_exports__, __webpack_require__) {

eval(__webpack_require__.ts("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   ConnectIt: function() { return /* binding */ ConnectIt; }\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"(app-pages-browser)/./node_modules/next/dist/compiled/react/jsx-dev-runtime.js\");\n/* harmony import */ var thirdweb_react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! thirdweb/react */ \"(app-pages-browser)/./node_modules/thirdweb/dist/esm/react/web/ui/ConnectWallet/ConnectButton.js\");\n/* harmony import */ var thirdweb_react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! thirdweb/react */ \"(app-pages-browser)/./node_modules/thirdweb/dist/esm/react/core/design-system/index.js\");\n/* harmony import */ var thirdweb_wallets__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! thirdweb/wallets */ \"(app-pages-browser)/./node_modules/thirdweb/dist/esm/wallets/create-wallet.js\");\n/* harmony import */ var _app_client__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/app/client */ \"(app-pages-browser)/./app/client.ts\");\n\n\n\n\n\nconst wallets = [\n    (0,thirdweb_wallets__WEBPACK_IMPORTED_MODULE_2__.createWallet)(\"io.metamask\"),\n    (0,thirdweb_wallets__WEBPACK_IMPORTED_MODULE_2__.createWallet)(\"com.coinbase.wallet\"),\n    (0,thirdweb_wallets__WEBPACK_IMPORTED_MODULE_2__.createWallet)(\"me.rainbow\"),\n    (0,thirdweb_wallets__WEBPACK_IMPORTED_MODULE_2__.createWallet)(\"io.rabby\"),\n    (0,thirdweb_wallets__WEBPACK_IMPORTED_MODULE_2__.createWallet)(\"io.zerion.wallet\")\n];\nfunction ConnectIt() {\n    return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(thirdweb_react__WEBPACK_IMPORTED_MODULE_3__.ConnectButton, {\n        client: _app_client__WEBPACK_IMPORTED_MODULE_1__.client,\n        wallets: wallets,\n        theme: (0,thirdweb_react__WEBPACK_IMPORTED_MODULE_4__.darkTheme)({\n            colors: {\n                accentText: \"#be33ff\"\n            }\n        }),\n        connectModal: {\n            size: \"wide\",\n            title: \"Connect to VeilX\",\n            showThirdwebBranding: false\n        }\n    }, void 0, false, {\n        fileName: \"C:\\\\Users\\\\ssach\\\\Personal+Courses\\\\Next\\\\VeilX\\\\web\\\\app\\\\contexts\\\\StateContext.tsx\",\n        lineNumber: 15,\n        columnNumber: 5\n    }, this);\n}\n_c = ConnectIt;\nvar _c;\n$RefreshReg$(_c, \"ConnectIt\");\n\n\n;\n    // Wrapped in an IIFE to avoid polluting the global scope\n    ;\n    (function () {\n        var _a, _b;\n        // Legacy CSS implementations will `eval` browser code in a Node.js context\n        // to extract CSS. For backwards compatibility, we need to check we're in a\n        // browser context before continuing.\n        if (typeof self !== 'undefined' &&\n            // AMP / No-JS mode does not inject these helpers:\n            '$RefreshHelpers$' in self) {\n            // @ts-ignore __webpack_module__ is global\n            var currentExports = module.exports;\n            // @ts-ignore __webpack_module__ is global\n            var prevSignature = (_b = (_a = module.hot.data) === null || _a === void 0 ? void 0 : _a.prevSignature) !== null && _b !== void 0 ? _b : null;\n            // This cannot happen in MainTemplate because the exports mismatch between\n            // templating and execution.\n            self.$RefreshHelpers$.registerExportsForReactRefresh(currentExports, module.id);\n            // A module can be accepted automatically based on its exports, e.g. when\n            // it is a Refresh Boundary.\n            if (self.$RefreshHelpers$.isReactRefreshBoundary(currentExports)) {\n                // Save the previous exports signature on update so we can compare the boundary\n                // signatures. We avoid saving exports themselves since it causes memory leaks (https://github.com/vercel/next.js/pull/53797)\n                module.hot.dispose(function (data) {\n                    data.prevSignature =\n                        self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports);\n                });\n                // Unconditionally accept an update to this module, we'll check if it's\n                // still a Refresh Boundary later.\n                // @ts-ignore importMeta is replaced in the loader\n                module.hot.accept();\n                // This field is set when the previous version of this module was a\n                // Refresh Boundary, letting us know we need to check for invalidation or\n                // enqueue an update.\n                if (prevSignature !== null) {\n                    // A boundary can become ineligible if its exports are incompatible\n                    // with the previous exports.\n                    //\n                    // For example, if you add/remove/change exports, we'll want to\n                    // re-execute the importing modules, and force those components to\n                    // re-render. Similarly, if you convert a class component to a\n                    // function, we want to invalidate the boundary.\n                    if (self.$RefreshHelpers$.shouldInvalidateReactRefreshBoundary(prevSignature, self.$RefreshHelpers$.getRefreshBoundarySignature(currentExports))) {\n                        module.hot.invalidate();\n                    }\n                    else {\n                        self.$RefreshHelpers$.scheduleUpdate();\n                    }\n                }\n            }\n            else {\n                // Since we just executed the code for the module, it's possible that the\n                // new exports made it ineligible for being a boundary.\n                // We only care about the case when we were _previously_ a boundary,\n                // because we already accepted this update (accidental side effect).\n                var isNoLongerABoundary = prevSignature !== null;\n                if (isNoLongerABoundary) {\n                    module.hot.invalidate();\n                }\n            }\n        }\n    })();\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiKGFwcC1wYWdlcy1icm93c2VyKS8uL2FwcC9jb250ZXh0cy9TdGF0ZUNvbnRleHQudHN4IiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7QUFBK0M7QUFDSjtBQUNLO0FBQ1Y7QUFFdEMsTUFBTUksVUFBVTtJQUNkRiw4REFBWUEsQ0FBQztJQUNiQSw4REFBWUEsQ0FBQztJQUNiQSw4REFBWUEsQ0FBQztJQUNiQSw4REFBWUEsQ0FBQztJQUNiQSw4REFBWUEsQ0FBQztDQUNkO0FBQ00sU0FBU0c7SUFDZCxxQkFDRSw4REFBQ0wseURBQWFBO1FBQ1pHLFFBQVFBLCtDQUFNQTtRQUNkQyxTQUFTQTtRQUNURSxPQUFPTCx5REFBU0EsQ0FBQztZQUNmTSxRQUFRO2dCQUFFQyxZQUFZO1lBQVU7UUFDbEM7UUFDQUMsY0FBYztZQUNaQyxNQUFNO1lBQ05DLE9BQU87WUFDUEMsc0JBQXNCO1FBQ3hCOzs7Ozs7QUFHTjtLQWZnQlAiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9fTl9FLy4vYXBwL2NvbnRleHRzL1N0YXRlQ29udGV4dC50c3g/OTVjMyJdLCJzb3VyY2VzQ29udGVudCI6WyJpbXBvcnQgeyBDb25uZWN0QnV0dG9uIH0gZnJvbSBcInRoaXJkd2ViL3JlYWN0XCI7XHJcbmltcG9ydCB7IGRhcmtUaGVtZSB9IGZyb20gXCJ0aGlyZHdlYi9yZWFjdFwiO1xyXG5pbXBvcnQgeyBjcmVhdGVXYWxsZXQgfSBmcm9tIFwidGhpcmR3ZWIvd2FsbGV0c1wiO1xyXG5pbXBvcnQgeyBjbGllbnQgfSBmcm9tIFwiQC9hcHAvY2xpZW50XCI7XHJcbmltcG9ydCB7IHVzZVRoZW1lIH0gZnJvbSBcIm5leHQtdGhlbWVzXCI7XHJcbmNvbnN0IHdhbGxldHMgPSBbXHJcbiAgY3JlYXRlV2FsbGV0KFwiaW8ubWV0YW1hc2tcIiksXHJcbiAgY3JlYXRlV2FsbGV0KFwiY29tLmNvaW5iYXNlLndhbGxldFwiKSxcclxuICBjcmVhdGVXYWxsZXQoXCJtZS5yYWluYm93XCIpLFxyXG4gIGNyZWF0ZVdhbGxldChcImlvLnJhYmJ5XCIpLFxyXG4gIGNyZWF0ZVdhbGxldChcImlvLnplcmlvbi53YWxsZXRcIiksXHJcbl07XHJcbmV4cG9ydCBmdW5jdGlvbiBDb25uZWN0SXQoKSB7XHJcbiAgcmV0dXJuIChcclxuICAgIDxDb25uZWN0QnV0dG9uXHJcbiAgICAgIGNsaWVudD17Y2xpZW50fVxyXG4gICAgICB3YWxsZXRzPXt3YWxsZXRzfVxyXG4gICAgICB0aGVtZT17ZGFya1RoZW1lKHtcclxuICAgICAgICBjb2xvcnM6IHsgYWNjZW50VGV4dDogXCIjYmUzM2ZmXCIgfSxcclxuICAgICAgfSl9XHJcbiAgICAgIGNvbm5lY3RNb2RhbD17e1xyXG4gICAgICAgIHNpemU6IFwid2lkZVwiLFxyXG4gICAgICAgIHRpdGxlOiBcIkNvbm5lY3QgdG8gVmVpbFhcIixcclxuICAgICAgICBzaG93VGhpcmR3ZWJCcmFuZGluZzogZmFsc2UsXHJcbiAgICAgIH19XHJcbiAgICAvPlxyXG4gICk7XHJcbn1cclxuIl0sIm5hbWVzIjpbIkNvbm5lY3RCdXR0b24iLCJkYXJrVGhlbWUiLCJjcmVhdGVXYWxsZXQiLCJjbGllbnQiLCJ3YWxsZXRzIiwiQ29ubmVjdEl0IiwidGhlbWUiLCJjb2xvcnMiLCJhY2NlbnRUZXh0IiwiY29ubmVjdE1vZGFsIiwic2l6ZSIsInRpdGxlIiwic2hvd1RoaXJkd2ViQnJhbmRpbmciXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///(app-pages-browser)/./app/contexts/StateContext.tsx\n"));

/***/ })

});