import { BASE_URL } from '@/config';
import axios from "axios"

export default {
    namespaced: true,
    state: {
        info:{},
        msg:''
    },
    getters:{
        getInfoProfile(state){
            return state.info
        },
        getMsgStatus(state){
            return state.msg
        }
    },
    mutations:{
        setInfoProfile(state, data){ state.info = data },
        setMsgStatus(state, msg){ state.msg = msg }
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