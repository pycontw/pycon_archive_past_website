!(function (e) {
  function r(data) {
    for (
      var r, n, f = data[0], d = data[1], l = data[2], i = 0, h = [];
      i < f.length;
      i++
    )
      (n = f[i]),
        Object.prototype.hasOwnProperty.call(o, n) && o[n] && h.push(o[n][0]),
        (o[n] = 0);
    for (r in d) Object.prototype.hasOwnProperty.call(d, r) && (e[r] = d[r]);
    for (v && v(data); h.length; ) h.shift()();
    return c.push.apply(c, l || []), t();
  }
  function t() {
    for (var e, i = 0; i < c.length; i++) {
      for (var r = c[i], t = !0, n = 1; n < r.length; n++) {
        var d = r[n];
        0 !== o[d] && (t = !1);
      }
      t && (c.splice(i--, 1), (e = f((f.s = r[0]))));
    }
    return e;
  }
  var n = {},
    o = { 82: 0 },
    c = [];
  function f(r) {
    if (n[r]) return n[r].exports;
    var t = (n[r] = { i: r, l: !1, exports: {} });
    return e[r].call(t.exports, t, t.exports, f), (t.l = !0), t.exports;
  }
  (f.e = function (e) {
    var r = [],
      t = o[e];
    if (0 !== t)
      if (t) r.push(t[2]);
      else {
        var n = new Promise(function (r, n) {
          t = o[e] = [r, n];
        });
        r.push((t[2] = n));
        var c,
          script = document.createElement("script");
        (script.charset = "utf-8"),
          (script.timeout = 120),
          f.nc && script.setAttribute("nonce", f.nc),
          (script.src = (function (e) {
            return (
              f.p +
              "" +
              {
                0: "5199eb6",
                1: "f55a243",
                4: "f147ea1",
                5: "f724e3f",
                6: "0ed53ea",
                7: "1b45683",
                8: "8059452",
                9: "698339b",
                10: "6a0294d",
                11: "e899bfd",
                12: "9b50bf0",
                13: "2a816a5",
                14: "91f6936",
                15: "7a6aeec",
                16: "272b678",
                17: "6c3500e",
                18: "11e1451",
                19: "e07246e",
                20: "19e72f2",
                21: "14b35f0",
                22: "4d28947",
                23: "3656a62",
                24: "99ba151",
                25: "9117dfe",
                26: "5e5b90d",
                27: "b838c99",
                28: "8d64bfa",
                29: "e9c65ca",
                30: "cb1a39e",
                31: "3dc09e9",
                32: "197ff1e",
                33: "22338f2",
                34: "be098dc",
                35: "1fa99a7",
                36: "82c301b",
                37: "f44c76e",
                38: "0d2d24b",
                39: "405cd3f",
                40: "c24bda0",
                41: "33b428d",
                42: "e5f554e",
                43: "912b5a4",
                44: "5cb1d54",
                45: "4e8c50d",
                46: "3197ad8",
                47: "7f6c65e",
                48: "5a3eb37",
                49: "fa24584",
                50: "fc5abb1",
                51: "bb27da8",
                52: "5d6358a",
                53: "75e3cc2",
                54: "164949b",
                55: "ab53167",
                56: "426be57",
                57: "45c3268",
                58: "ebbb030",
                59: "1871d51",
                60: "bfeaf8a",
                61: "bfb90a5",
                62: "2a8b2bc",
                63: "d6dbe88",
                64: "0ade89c",
                65: "41dc9d7",
                66: "394dbd6",
                67: "0de669c",
                68: "5067675",
                69: "57c0518",
                70: "30b7dd9",
                71: "9b33a17",
                72: "b75dc61",
                73: "0fcb7a3",
                74: "a6e770d",
                75: "fcc2732",
                76: "e5e8831",
                77: "504a1e9",
                78: "b217355",
                79: "58d5cb8",
                80: "0d23fd9",
                81: "51cc9c0",
                84: "6972eca",
              }[e] +
              ".js"
            );
          })(e));
        var d = new Error();
        c = function (r) {
          (script.onerror = script.onload = null), clearTimeout(l);
          var t = o[e];
          if (0 !== t) {
            if (t) {
              var n = r && ("load" === r.type ? "missing" : r.type),
                c = r && r.target && r.target.src;
              (d.message =
                "Loading chunk " + e + " failed.\n(" + n + ": " + c + ")"),
                (d.name = "ChunkLoadError"),
                (d.type = n),
                (d.request = c),
                t[1](d);
            }
            o[e] = void 0;
          }
        };
        var l = setTimeout(function () {
          c({ type: "timeout", target: script });
        }, 12e4);
        (script.onerror = script.onload = c), document.head.appendChild(script);
      }
    return Promise.all(r);
  }),
    (f.m = e),
    (f.c = n),
    (f.d = function (e, r, t) {
      f.o(e, r) || Object.defineProperty(e, r, { enumerable: !0, get: t });
    }),
    (f.r = function (e) {
      "undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 });
    }),
    (f.t = function (e, r) {
      if ((1 & r && (e = f(e)), 8 & r)) return e;
      if (4 & r && "object" == typeof e && e && e.__esModule) return e;
      var t = Object.create(null);
      if (
        (f.r(t),
        Object.defineProperty(t, "default", { enumerable: !0, value: e }),
        2 & r && "string" != typeof e)
      )
        for (var n in e)
          f.d(
            t,
            n,
            function (r) {
              return e[r];
            }.bind(null, n)
          );
      return t;
    }),
    (f.n = function (e) {
      var r =
        e && e.__esModule
          ? function () {
              return e.default;
            }
          : function () {
              return e;
            };
      return f.d(r, "a", r), r;
    }),
    (f.o = function (object, e) {
      return Object.prototype.hasOwnProperty.call(object, e);
    }),
    (f.p = "https://tw.pycon.org/2021/_nuxt/"),
    (f.oe = function (e) {
      throw (console.error(e), e);
    });
  var d = (window.webpackJsonp = window.webpackJsonp || []),
    l = d.push.bind(d);
  (d.push = r), (d = d.slice());
  for (var i = 0; i < d.length; i++) r(d[i]);
  var v = l;
  t();
})([]);