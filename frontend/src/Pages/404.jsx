import { CenterContainer, Text, VBox } from "@liro_u/react-components";
import React from "react";

import { useTranslation } from "react-i18next";

const Page404 = () => {

  const { t } = useTranslation();

  return (
    <CenterContainer>
      <VBox>
        <CenterContainer>
          <Text text="404" fontSize="50px" fontWeight="bold" />
        </CenterContainer>
        <CenterContainer>
          <Text text={t('errors.404error')} />
        </CenterContainer>
      </VBox>
    </CenterContainer>
  );
};

export default Page404;
