// import './codemirror.js'
// import './simple.js';
alert('didu run');
CodeMirror.defineSimpleMode("spthy", {
    // The start state contains the rules that are initially used
    start: [
        // The regex matches the token, the token property contains the type
        { regex: /"(?:[^\\]|\\.)*?(?:"|$)/, token: "string" },
        // You can match multiple tokens at once. Note that the captured
        // groups must span the whole string in this case
        {
            regex: /\b(axiom|restriction|lemma|sources|use_induction|reuse|hide_lemma|left|right|builtins|protocol|property|subsection|section|text)\b/,
            token: ["keyword", null, "variable-2"]
        },
        // {
        //   regex: /\b(xor|aenc|adec|senc|sdec|sign|verify|Eq|eq|hashing|signing|revealing-signing|diffie-hellman|symmetric-encryption|asymmetric-encryption|multiset|bilinear-pairing|h|H|sk|pk|Fr|In|Out|IN|OUT)\b/,
        //   token: "variable.language"
        // },
        // Rules are matched in the order in which they appear, so there is
        // no ambiguity between this one and the one above
        {
            regex: /\b(equations|functions|builtins|protocol|property|theory|begin|end|subsection|section|text|rule|pb|lts|exists-trace|all-traces|enable|assertions|modulo|default_rules|anb-proto|in|let|Fresh|fresh|Public|public)\b/,
            token: "keyword.control"
        },
        // { regex: /true|false|null|undefined/, token: "atom" },
        {
            regex: /0x[a-f\d]+|[-+]?(?:\.\d+|\d+\.?\d*)(?:e[-+]?\d+)?/i,
            token: "number"
        },
        { regex: /\b(in|let|begin|end)\b/, token: "constant.language" },
        { regex: /\/\/.*/, token: "comment" },
        // { regex: /\/(?:[^\\]|\\.)*?\//, token: "variable-3" },
        // A next property will cause the mode to move to a different state
        { regex: /\/\*/, token: "comment", next: "comment" },
        { regex: /[-+\/*=<>!]+/, token: "operator" },
        // indent and dedent properties guide autoindentation
        { regex: /[\{\[\(]/, indent: true },
        { regex: /[\}\]\)]/, dedent: true },
        { regex: /[a-z$][\w$]*/, token: "variable" },
        // You can embed other modes with the mode property. This rule
        // causes all code between << and >> to be highlighted with the XML
        // mode.
        { regex: /<</, token: "meta", mode: { spec: "xml", end: />>/ } }
    ],
    // The multi-line comment state.
    comment: [
        { regex: /.*?\*\//, token: "comment", next: "start" },
        { regex: /.*/, token: "comment" }
    ],
    // The meta property contains global information about the mode. It
    // can contain properties like lineComment, which are supported by
    // all modes, and also directives like dontIndentStates, which are
    // specific to simple modes.
    meta: {
        dontIndentStates: ["comment"],
        lineComment: "//"
    }
});
