from __future__ import annotations

from collections import defaultdict

from datasets import DatasetDict, load_dataset

from mteb.abstasks.TaskMetadata import TaskMetadata

from ....abstasks.AbsTaskRetrieval import AbsTaskRetrieval


def load_retrieval_data(dataset_path, dataset_revision, qrel_revision, eval_splits):
    eval_split = eval_splits[0]
    dataset = load_dataset(dataset_path, revision=dataset_revision)
    qrels = load_dataset(dataset_path + "-qrels", revision=qrel_revision)[eval_split]

    corpus = {e["id"]: {"text": e["text"]} for e in dataset["corpus"]}
    queries = {e["id"]: e["text"] for e in dataset["queries"]}
    relevant_docs = defaultdict(dict)
    for e in qrels:
        relevant_docs[e["qid"]][e["pid"]] = e["score"]

    corpus = DatasetDict({eval_split: corpus})
    queries = DatasetDict({eval_split: queries})
    relevant_docs = DatasetDict({eval_split: relevant_docs})
    return corpus, queries, relevant_docs


class T2Retrieval(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="T2Retrieval",
        description="T2Ranking: A large-scale Chinese Benchmark for Passage Ranking",
        reference="https://arxiv.org/abs/2304.03679",
        dataset={
            "path": "C-MTEB/T2Retrieval",
            "revision": "8731a845f1bf500a4f111cf1070785c793d10e64",
            "qrel_revision": "1c83b8d1544e529875e3f6930f3a1fcf749a8e97",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation="""@misc{xie2023t2ranking,
      title={T2Ranking: A large-scale Chinese Benchmark for Passage Ranking},
      author={Xiaohui Xie and Qian Dong and Bingning Wang and Feiyang Lv and Ting Yao and Weinan Gan and Zhijing Wu and Xiangsheng Li and Haitao Li and Yiqun Liu and Jin Ma},
      year={2023},
      eprint={2304.03679},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}""",
        prompt={
            "query": "Given a Chinese search query, retrieve web passages that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True


class MMarcoRetrieval(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="MMarcoRetrieval",
        description="MMarcoRetrieval",
        reference="https://arxiv.org/abs/2309.07597",
        dataset={
            "path": "C-MTEB/MMarcoRetrieval",
            "revision": "539bbde593d947e2a124ba72651aafc09eb33fc2",
            "qrel_revision": "bae08bb7bddbedb96c7e7db52018a55167b67f89",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation="""@misc{xiao2024cpack,
      title={C-Pack: Packaged Resources To Advance General Chinese Embedding},
      author={Shitao Xiao and Zheng Liu and Peitian Zhang and Niklas Muennighoff and Defu Lian and Jian-Yun Nie},
      year={2024},
      eprint={2309.07597},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}""",
        prompt={
            "query": "Given a web search query, retrieve relevant passages that answer the query"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True


class DuRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="DuRetrieval",
        description="A Large-scale Chinese Benchmark for Passage Retrieval from Web Search Engine",
        reference="https://aclanthology.org/2022.emnlp-main.357.pdf",
        dataset={
            "path": "C-MTEB/DuRetrieval",
            "revision": "a1a333e290fe30b10f3f56498e3a0d911a693ced",
            "qrel_revision": "497b7bd1bbb25cb3757ff34d95a8be50a3de2279",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation="""@misc{qiu2022dureaderretrieval,
      title={DuReader_retrieval: A Large-scale Chinese Benchmark for Passage Retrieval from Web Search Engine},
      author={Yifu Qiu and Hongyu Li and Yingqi Qu and Ying Chen and Qiaoqiao She and Jing Liu and Hua Wu and Haifeng Wang},
      year={2022},
      eprint={2203.10232},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}""",
        prompt={
            "query": "Given a Chinese search query, retrieve web passages that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True


class CovidRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="CovidRetrieval",
        description="COVID-19 news articles",
        reference="https://arxiv.org/abs/2203.03367",
        dataset={
            "path": "C-MTEB/CovidRetrieval",
            "revision": "1271c7809071a13532e05f25fb53511ffce77117",
            "qrel_revision": "a9f41b7cdf24785531d12417ce0d1157ed4b39ca",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a question on COVID-19, retrieve news articles that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True


class CmedqaRetrieval(AbsTaskRetrieval):
    metadata = TaskMetadata(
        name="CmedqaRetrieval",
        description="Online medical consultation text. Used the CMedQAv2 as its underlying dataset.",
        reference="https://aclanthology.org/2022.emnlp-main.357.pdf",
        dataset={
            "path": "C-MTEB/CmedqaRetrieval",
            "revision": "cd540c506dae1cf9e9a59c3e06f42030d54e7301",
            "qrel_revision": "279d737f36c731c8ff6e2b055f31fe02216fa23d",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
        date=None,
        domains=["Medical", "Written"],
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a Chinese community medical question, retrieve replies that best answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True


class EcomRetrieval(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="EcomRetrieval",
        description="EcomRetrieval",
        reference="https://arxiv.org/abs/2203.03367",
        dataset={
            "path": "C-MTEB/EcomRetrieval",
            "revision": "687de13dc7294d6fd9be10c6945f9e8fec8166b9",
            "qrel_revision": "39c90699b034ec22ac45b3abf5b0bbb5ffd421f9",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a user query from an e-commerce website, retrieve description sentences of relevant products"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True


class MedicalRetrieval(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="MedicalRetrieval",
        description="MedicalRetrieval",
        reference="https://arxiv.org/abs/2203.03367",
        dataset={
            "path": "C-MTEB/MedicalRetrieval",
            "revision": "2039188fb5800a9803ba5048df7b76e6fb151fc6",
            "qrel_revision": "37b8efec53c54c3d9c6af212f6710b62ccdf895c",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a medical question, retrieve user replies that best answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True

class PplxRetrievalOneThousandth(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="PplxRetrievalOneThousandth",
        description="PplxRetrievalOneThousandth",
        reference="https://perplexity.ai",
        dataset={
            "path": "jinaai/pplx_jina_onethousandth",
            "revision": "e1d8e54a89401678b874773506cfa0a905aa5f27",
            "qrel_revision": "521e25f2490224c319720d9f901061664b1483b7",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["en"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a question, retrieve internet documents that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True

class PplxRetrievalV2All(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="PplxRetrievalV2All",
        description="PplxRetrievalV2All",
        reference="https://perplexity.ai",
        dataset={
            "path": "jinaai/pplx_jina_v2_all",
            "revision": "91f93bf801e6eb13f98180e07becb7bd4a9a7a0f",
            "qrel_revision": "5f945c972cbf0ffc3c2b05cbf4ea92de1d58646f",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["en"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a question, retrieve internet documents that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True

class PplxRetrievalV2En(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="PplxRetrievalV2En",
        description="PplxRetrievalV2En",
        reference="https://perplexity.ai",
        dataset={
            "path": "jinaai/pplx_jina_v2_en",
            "revision": "af657f7cb7d0692270da768510b42f4783edc919",
            "qrel_revision": "6f81f26d242cc5fddf85b7f0b9eab4e8f3df9d36",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["en"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a question, retrieve internet documents that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True

class PplxRetrievalV2NonEn(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="PplxRetrievalV2NonEn",
        description="PplxRetrievalV2NonEn",
        reference="https://perplexity.ai",
        dataset={
            "path": "jinaai/pplx_jina_v2_non_en",
            "revision": "65584774b825665801616b75632a586d5d6e0579",
            "qrel_revision": "0c740faf18f963726163240653549df725b2bb91",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["en"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a question, retrieve internet documents that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True

class PplxRetrievalV2SmallNonEn(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="PplxRetrievalV2SmallNonEn",
        description="PplxRetrievalV2SmallNonEn",
        reference="https://perplexity.ai",
        dataset={
            "path": "jinaai/pplx_jina_v2_small_non_en",
            "revision": "dc6ce0291f055ef7177d4d8176e9e6241b8f6805",
            "qrel_revision": "3e3c5c66e35128ce2db6bb1f50e6f9ad309b7cf1",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["en"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a question, retrieve internet documents that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True


class PplxRetrievalNano(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="PplxRetrievalNano",
        description="PplxRetrievalNano",
        reference="https://perplexity.ai",
        dataset={
            "path": "jinaai/pplx_jina_nano",
            "revision": "ae7b0309c7b49497d5521293ecbe198d22a6bf3f",
            "qrel_revision": "b35ecf07bf0a6c3837bdb97368bb6074ae6e0e16",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["en"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a question, retrieve internet documents that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True

class PplxRetrieval(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="PplxRetrieval",
        description="PplxRetrieval",
        reference="https://perplexity.ai",
        dataset={
            "path": "jinaai/pplx_jina_onethousandth",
            "revision": "e1d8e54a89401678b874773506cfa0a905aa5f27",
            "qrel_revision": "c43f10b77d28bf4ae6d97b0c16c46fd7f62fd5ac",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["en"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a question, retrieve internet documents that answer the question"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True


class VideoRetrieval(AbsTaskRetrieval):
    ignore_identical_ids = True

    metadata = TaskMetadata(
        name="VideoRetrieval",
        description="VideoRetrieval",
        reference="https://arxiv.org/abs/2203.03367",
        dataset={
            "path": "C-MTEB/VideoRetrieval",
            "revision": "58c2597a5943a2ba48f4668c3b90d796283c5639",
            "qrel_revision": "faa71382b6a29cf1778d1f436b963e75cb5b927c",
        },
        type="Retrieval",
        category="s2p",
        modalities=["text"],
        eval_splits=["dev"],
        eval_langs=["cmn-Hans"],
        main_score="ndcg_at_10",
        date=None,
        domains=None,
        task_subtypes=None,
        license=None,
        annotations_creators=None,
        dialect=None,
        sample_creation=None,
        bibtex_citation=None,
        prompt={
            "query": "Given a video search query, retrieve the titles of relevant videos"
        },
    )

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        self.corpus, self.queries, self.relevant_docs = load_retrieval_data(
            self.metadata_dict["dataset"]["path"],
            self.metadata_dict["dataset"]["revision"],
            self.metadata_dict["dataset"]["qrel_revision"],
            self.metadata_dict["eval_splits"],
        )
        self.data_loaded = True
