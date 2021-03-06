<template>
  <ControlPanelContentFrame>
    <template slot="title">
      Tutorial Anchors
    </template>
    <template>
      <q-table
        :data="tableContent"
        :columns="columns"
        :pagination="pagination"
        :loading="loadingContent"
        no-data-label="No tutorials are found."
        row-key="id"
        separator="cell"
        class="custom-table"
      >
        <template v-slot:top>
          <RefreshButton :fetch-func="fetchTutorials"></RefreshButton>
          <AddNewButton :create-func="createTutorial" />
        </template>
        <template v-slot:header="props">
          <AllTableHeader :passed-props="props" />
        </template>
        <template v-slot:body="props">
          <q-tr :props="props">
            <!-- tutorial name -->
            <q-td key="name" :props="props">
              <OpenInEditorButton
                :label="props.row.name"
                :routePath="{
                  name: 'Tutorial Anchor Editor',
                  params: { id: props.row.id },
                }"
              />
            </q-td>

            <q-td key="rank" :props="props">
              <RankDisplay :rank="props.row.rank" />
            </q-td>

            <!-- tutorial published -->
            <q-td key="isPublished" :props="props">
              {{ props.row.isPublished ? '✅' : '❌' }}
            </q-td>

            <!-- tutorial url -->
            <q-td key="url" :props="props">
              <OpenInPageButton
                :label="props.row.url"
                :routePath="{
                  name: 'Tutorial',
                  params: { lang: $i18n.locale, url: props.row.url },
                }"
              />
            </q-td>

            <!-- tutorial id -->
            <q-td key="id" :props="props">
              {{ props.row.id }}
            </q-td>

            <DeleteTableCell
              :message="
                `Do you want to delete tutorial anchor '${props.row.name} with id '${props.row.id}'?`
              "
              :id="props.row.id"
              content-type="TUTORIAL_ANCHOR"
              :final-callback="fetchTutorials"
            />
          </q-tr>
        </template>
      </q-table>
    </template>
  </ControlPanelContentFrame>
</template>

<script>
  import { apiCaller } from '@/services/apis';
  import { tutorialAnchorListQuery } from '@/services/queries';
  import { errorDialog, resolveAndOpenLink } from '@/services/helpers';
  import loadingMixin from '../mixins/LoadingMixin.vue';
  import { newModelUUID } from '@/services/params';
  import AllTableHeader from '@/components/ControlPanel/parts/table/AllTableHeader';

  export default {
    mixins: [loadingMixin],
    components: {
      RankDisplay: () => import('@/components/framework/RankDisplay.vue'),
      DeleteTableCell: () =>
        import('@/components/ControlPanel/parts/table/DeleteTableCell'),
      AllTableHeader,
      AddNewButton: () => import('../parts/buttons/AddNewButton'),
      ControlPanelContentFrame: () =>
        import('../frames/ControlPanelContentFrame.vue'),
      RefreshButton: () => import('../parts/buttons/RefreshButton.vue'),
      OpenInEditorButton: () =>
        import('../parts/buttons/OpenInEditorButton.vue'),
      OpenInPageButton: () => import('../parts/buttons/OpenInPageButton.vue'),
    },
    data() {
      return {
        columns: [
          {
            name: 'name',
            label: 'Name',
            field: 'name',
            align: 'center',
            sortable: true,
          },
          {
            name: 'rank',
            label: 'Rank',
            field: 'rank',
            align: 'center',
            sortable: true,
            sort: (a, b) => {
              if (a.level === b.level) {
                if (a.section === b.section) {
                  return 0;
                }

                return a.section < b.section ? -1 : 1;
              }

              return a.level < b.level ? -1 : 1;
            },
          },
          {
            name: 'isPublished',
            label: 'Published?',
            field: 'isPublished',
            align: 'center',
          },
          {
            name: 'url',
            label: 'URL',
            field: 'url',
            align: 'center',
            // TODO add typewriter font style
          },
          {
            name: 'id',
            label: 'ID',
            field: 'id',
            align: 'center',
            required: true,
            // TODO add typewriter font style
          },
        ],
        pagination: {
          sortBy: 'rank',
          rowsPerPage: 20,
        },
        tableContent: [],
        // TODO add trans to no data label
      };
    },
    methods: {
      fetchTutorials() {
        this.startLoading();
        apiCaller(tutorialAnchorListQuery)
          .then((data) => {
            if (!data || !('allTutorialInfo' in data)) {
              throw Error('Invalid data returned.');
            }

            this.tableContent = data['allTutorialInfo'];
          })
          .catch((err) => {
            this.tableContent = [];
            errorDialog({
              message: `Cannot load tutorials. ${err}`,
            });
          })
          .finally(() => {
            this.finishedLoading();
          });
      },
      createTutorial() {
        resolveAndOpenLink({
          name: 'Tutorial Anchor Editor',
          params: { id: newModelUUID },
        });
      },
    },
    mounted() {
      this.fetchTutorials();
    },
  };
</script>
