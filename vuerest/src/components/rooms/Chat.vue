<template>
    <mu-col span="1" sm="9" align="end">
        <mu-container style="border: .5px solid black;">
            <div v-for="dialog in chats">
                <p><strong>{{dialog.user.username}}</strong></p>
                <p>{{dialog.text}}</p>
                <span>{{dialog.date}}</span>
            </div>
        </mu-container>
        <mu-text-field 
            multi-line 
            :rows="3" 
            prop="model"
            :rows-max="6" 
            v-model="form.textarea" 
            placeholder="Введите текст сообщения">
        </mu-text-field>
        <mu-button color="blue" @click="sendMessage">Send<mu-icon right value="send"></mu-icon>
        </mu-button>
    </mu-col>
</template>
<script>
export default {
    name: "Chat",
    props: {
        pk: '',
    },
    data() {
        return {
            chats: '',
            form: {
                textarea: '',
            }
        }
    },
    created() {
        $.ajaxSetup({
            headers: { 'Authorization': 'Token ' + sessionStorage.getItem('auth_token') }
        })
        this.loadChat()
    },
    methods: {
        loadChat() {
            $.ajax({
                url: 'http://localhost:5555/api/v1/chat/chat/',
                type: 'GET',
                data: {
                    room: this.pk,
                },
                success: (response) => {
                    this.chats = response.data.data
                }
            })
        },
        sendMessage() {
            $.ajax({
                url: 'http://localhost:5555/api/v1/chat/chat/',
                type: 'POST',
                data: {
                    room: this.pk,
                    text: this.form.textarea,
                },
                success: (response) => {
                    console.log(response.data)
                }
            })
        }
    }
}

</script>
<style scoped>
</style>
