<template>
    <mu-col span="1" sm="9">
        <mu-container ref="container" class="messages" align="end">
            <mu-load-more>
                <div v-for="dialog in chats">
                    <p><strong>{{dialog.user.username}}</strong></p>
                    <p>{{dialog.text}}</p>
                    <span>{{dialog.date}}</span>
                    <mu-divider />
                </div>
            </mu-load-more>
        </mu-container>
        <mu-container class="text mt-2">
            <mu-text-field multi-line :rows="4" prop="model" :rows-max="6" v-model="form.textarea" placeholder="Введите текст сообщения">
            </mu-text-field>
            <mu-button color="blue" @click="sendMessage">Send<mu-icon right value="send"></mu-icon>
            </mu-button>
        </mu-container>
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
.text {

}
</style>