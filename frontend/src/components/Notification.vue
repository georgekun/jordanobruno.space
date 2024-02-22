<template>
    <v-dialog width="450" v-model="isActive" theme="dark">
      <v-card title="">
        <v-card-text>
            {{ getMsgStatus }}
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            text="закрыть"
            @click="closeDialog"
          ></v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
import { mapGetters, mapMutations } from 'vuex'

export default{
    name: "Notification",
    data(){
        return{
            isActive:false
        }
    },
    computed:{
        ...mapGetters('main', ['getMsgStatus'])
    },
    methods: {
        ...mapMutations('main', ['setMsgStatus']),
        closeDialog(){
            this.setMsgStatus('')
            this.isActive = false
        }
    },
    watch:{
        getMsgStatus:{
            handler(newValue){
                if(newValue != ''){
                    this.isActive = true
                }
            },
            deep:true
        }
    }
}
</script>

<style scoped>
</style>