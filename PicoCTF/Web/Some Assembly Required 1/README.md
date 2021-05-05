# Some Assembly Required 1

```
Author: Sears Schulz
Description

http://mercury.picoctf.net:36152/index.html
```

```js
const original_list = ['value', '2wfTpTR', 'instantiate', '275341bEPcme', 'innerHTML', '1195047NznhZg', '1qfevql', 'input', '1699808QuoWhA', 'Correct!', 'check_flag', 'Incorrect!', './JIFxzHyW8W', '23SMpAuA', '802698XOMSrr', 'charCodeAt', '474547vVoGDO', 'getElementById', 'instance', 'copy_char', '43591XxcWUl', '504454llVtzW', 'arrayBuffer', '2NIQmVj', 'result'];

const my_function = function(arg1, arg2) {
    arg1 = arg1 - 470;
    let returnval = original_list[arg1];
    return returnval;
};
(function(arg1, arg2) {
    const my_function_copy = my_function;
    while (!![]) {
        try {
            const weird_var = -parseInt('504454llVtzW') + parseInt('2NIQmVj') + -parseInt('1195047NznhZg') * -parseInt('275341bEPcme') + -parseInt('./JIFxzHyW8W') * -parseInt('23SMpAuA') + -parseInt('1699808QuoWhA') * parseInt('check_flag') + parseInt('instantiate') * parseInt('43591XxcWUl') + -parseInt('charCodeAt');
            if (weird_var === arg2) break;
            else arg1['push'](arg1['shift']());
        } catch (_0x41d31a) {
            arg1['push'](arg1['shift']());
        }
    }
}(original_list, 0x994c3));

let exports;
(async () => {
    const my_function_copy = my_function;
    let _0x5f0229 = await fetch('copy_char'),
        _0x1d99e9 = await WebAssembly['Correct!'](await _0x5f0229['innerHTML']()),
        _0x1f8628 = _0x1d99e9['value'];
    exports = _0x1f8628['exports'];
})();

function onButtonPress() {
    const function_as_variable = my_function;

    let input_box = document['getElementById']('802698XOMSrr')['input'];

    for (let i = 0; i < input_box['length']; i++) {
        exports['2wfTpTR'](input_box['arrayBuffer'](i), i);
    }

    exports['copy_char'](0, input_box['length']), exports[function_as_variable(0x1e7)]() == 0x1 ? document[function_as_variable(0x1ee)](function_as_variable(0x1dc))[function_as_variable(0x1e1)] = function_as_variable(0x1e6) : document[function_as_variable(0x1ee)](function_as_variable(0x1dc))[function_as_variable(0x1e1)] = function_as_variable(0x1e8);
}
```

Note, this above was not needed. the flag is simply stored in a wasm file on the page

# Flag:

picoCTF{d88090e679c48f3945fcaa6a7d6d70c5}