import { BASE_URL } from '@/config';
import axios from "axios"

export default {
    namespaced: true,
    state: {
        info:{}
    },
    getters:{
        getInfoProfile(state){
            return state.info
        }
    },
    mutations:{
        setInfoProfile(state, data){ state.info = data }
    },
    actions:{
        GET_INFO_PROFILE_FROM_API({ commit }){
            const url = BASE_URL + 'personal/profile/'
            axios.get(url)
                .then( r => commit('setInfoProfile', r.data) )
                .catch( e => console.log(e) )
        }
    }
}