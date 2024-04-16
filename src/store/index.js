import {createStore} from "vuex"

const store = createStore({
    state: {
        current_ft: 'V0',
        current_ft_name: 'PVC连续',
        drop_atype_show: false
    },
    mutations: {
        update_current_ft(state, future) {
            state.current_ft = future.symbol
            state.current_ft_name = future.name
        },
        change_atype_vis(state, vis) {
            state.drop_atype_show = vis
        }
    },
})

export default store