<template>
  <q-card>
    <q-card-section>
      <q-file
        ref="filePicker"
        v-model="files"
        :readonly="loadingContent"
        :disable="loadingContent"
        :loading="loadingContent"
        multiple
        outlined
        clearable
        counter
        use-chips
        label="Select
      the files you want to upload."
        hint="You can select multiple files at once."
        append
        :max-total-size="10485760"
        class="full-width"
      >
        <template v-slot:prepend>
          <q-icon name="attach_file" @click.stop />
        </template>
        <template v-slot:append>
          <q-icon name="add" @click.stop />
        </template>
        <template v-slot:after>
          <q-btn @click="fileHandler" round dense flat icon="send" />
        </template>
      </q-file>
    </q-card-section>
  </q-card>
</template>

<script>
  import { fileUploadAction } from '../../mixins/UploadHandler';
  import loadingMixin from '../../mixins/LoadingMixin';
  import { errorDialog } from '@/services/helpers';
  export default {
    mixins: [loadingMixin],
    props: {
      finalCallback: {
        type: Function,
        default: () => () => null,
      },
    },
    data() {
      return {
        files: [],
      };
    },
    methods: {
      fileHandler() {
        this.startLoading();
        fileUploadAction(this.files)
          .then(() => {
            this.files = [];
          })
          .catch((err) => {
            errorDialog({
              message: `An error occurs during uploading files. ${err}`,
            });
          })
          .finally(() => {
            this.finishedLoading();
            this.finalCallback();
          });
      },
    },
  };
</script>
