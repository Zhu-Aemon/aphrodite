import {createStore} from "vuex"

const store = createStore({
    state: {
        current_ft: 'V0',
    },
    mutations: {
        update_current_ft(state, symbol) {
            state.current_ft = symbol
        },
    },
})

export default store