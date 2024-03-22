from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from typing import Optional, List, Any, Mapping


class CustomLLM(LLM):  # 这个类 CustomLLM 继承了 LLM 类，并增加了一个新的类变量 n。
    n: int  # 类变量，表示一个整数

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
            self,
            prompt: str,  # 输入的提示字符串
            stop: Optional[List[str]] = None,  # 可选的停止字符串列表，默认为 None
            run_manager: Optional[CallbackManagerForLLMRun] = None,  # 可选的回调管理器，默认为 None
            **kwargs: Any,
    ) -> str:
        # 如果 stop 参数不为 None，则抛出 ValueError 异常
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        return prompt[: self.n]  # 返回 prompt 字符串的前 n 个字符

    @property  # 一个属性装饰器，用于获取 _identifying_params 的值
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""  # 这个方法的文档字符串，说明这个方法的功能是获取标识参数
        return {"n": self.n}  # 返回一个字典，包含 n 的值
