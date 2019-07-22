<template>
    <RoomSlot>
        <mu-col span="1" sm="9">
            <AddUsers :room='pk' />
            <mu-container ref="container" class="messages" align="end">
                <div v-for="dialog in chats" v-bind:key="dialog">
                    <p><strong>{{dialog.user.username}}</strong></p>
                    <p>{{dialog.text}}</p>
                    <span>{{dialog.date}}</span>
                    <mu-divider />
                </div>
            </mu-container>
            <mu-container class="text mt-3">
                <mu-text-field class="textbase" multi-line prop="model" :rows="4" :rows-max="6" v-model="form.textarea"
                    placeholder="Введите текст сообщения">
                </mu-text-field>
                <mu-button color="blue" @click="sendMessage">Send<mu-icon right value="send"></mu-icon>
                </mu-button>
            </mu-container>
        </mu-col>
    </RoomSlot>
</template>
<script>
    import RoomSlot from '@/components/rooms/Room'
    import AddUsers from './AddUsers'
    export default {
        name: "Chat",
        props: {
            pk: '',
        },
        components: {
            AddUsers,
            RoomSlot
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
                headers: {
                    'Authorization': 'Token ' + sessionStorage.getItem('auth_token')
                }
            })
            this.loadChat()
            setInterval(() => {
                this.loadChat()
            }, 2000)
        },
        methods: {
            loadChat() {
                $.ajax({
                    url: 'http://localhost:5555/api/v1/chat/chat/',
                    type: 'GET',
                    data: {
                        room: this.$route.params.pk,
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
                        room: this.$route.params.pk,
                        text: this.form.textarea,
                    },
                    success: (response) => {
                        this.loadChat()
                    },
                    error: (response) => {
                        alert(response.statusText)
                    }
                })
            }
        }
    }
</script>
<style scoped>
    .text {
        width: 100%;
        display: flex;
        flex-direction: column;
    }

    .textbase {
        width: 100%;
    }

    .messages {
        display: flex;
        flex-direction: column;
    }
</style>