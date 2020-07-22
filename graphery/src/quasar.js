import Vue from 'vue';

import './styles/quasar.sass';
import '@quasar/extras/mdi-v5/mdi-v5.css';
import '@quasar/extras/material-icons/material-icons.css';
import {
  Quasar,
  QLayout,
  QHeader,
  QDrawer,
  QPageContainer,
  QPage,
  QToolbar,
  QToolbarTitle,
  QBtn,
  QIcon,
  QList,
  QItem,
  QItemSection,
  QItemLabel,
  // My extensions
  QBar,
  QIntersection,
  QCard,
  QCardSection,
  QCardActions,
  QChip,
  QInput,
  QFooter,
  QTooltip,
  QBtnDropdown,
  QBtnGroup,
  QDialog,
  QSlideTransition,
  QSeparator,
  QSelect,
  QInnerLoading,
  QSpinnerPie,
  QPageSticky,
  QCircularProgress,
  QImg,
  QAvatar,
  QPagination,
  QResizeObserver,
  QSplitter,
  QSpace,
  QSlider,
  QToggle,
  QExpansionItem,
  QVirtualScroll,
  QFab,
  QFabAction,
  QAjaxBar,
  QForm,
  QTable,
  QTh,
  QTr,
  QTd,
  // My plugins
  Notify,
  // My directive
  ClosePopup,
} from 'quasar';

Vue.use(Quasar, {
  config: {},
  components: {
    QLayout,
    QHeader,
    QDrawer,
    QPageContainer,
    QPage,
    QToolbar,
    QToolbarTitle,
    QBtn,
    QIcon,
    QList,
    QItem,
    QItemSection,
    QItemLabel,
    // my addons
    QBar,
    QIntersection,
    QCard,
    QCardSection,
    QCardActions,
    QChip,
    QInput,
    QFooter,
    QTooltip,
    QBtnDropdown,
    QBtnGroup,
    QDialog,
    QSlideTransition,
    QSeparator,
    QSelect,
    QInnerLoading,
    QSpinnerPie,
    QPageSticky,
    QCircularProgress,
    QImg,
    QAvatar,
    QPagination,
    QResizeObserver,
    QSplitter,
    QSpace,
    QSlider,
    QToggle,
    QExpansionItem,
    QVirtualScroll,
    QFab,
    QFabAction,
    QAjaxBar,
    QForm,
    QTable,
    QTh,
    QTr,
    QTd,
  },
  directives: { ClosePopup },
  plugins: { Notify },
});
